"""
Opencv.
Image datas is ndarray.
"""

import math
import os
import sys

import cv2 as cv
import numpy as np

global_img = 0  # Used click_event function.


def main():

    file_path = r'Lenna.png'#input('file path -> ')
    img = cv.imread(file_path)
    print('type', img.dtype,
          '\n' 'size', img.size,
          '\n' 'shape', img.shape,  # (height, width, color)
          )

    # Edit images.
    img_edited = edit(img)
    cv.imshow('image', img_edited)
    cv.waitKey(0)  # Wait keys.
    cv.destroyAllWindows()
    draw(img)
    mouse_event(img)
    trackbar(img)

    # Read a BGRA image as BGR.
    # Transparent background be brack.
    file_path = r'Canon.png'#input('file path -> ')
    img2 = cv.imread(file_path)
    img = combine(img, img2)

    cv.imshow('image', img)
    cv.waitKey(0)  # Wait until to get any keys.
    cv.destroyAllWindows()
    cv.imwrite('test.png', img)

    # Video.
    video()


def edit(image):

    img = image

    # Resize.
    #img = cv.resize(img, (100, 100))
    img = cv.resize(img, dsize=None, fx=1.5, fy=1.5)

    # Trim.
    img = img[:512, :512]

    # Flip.
    img = cv.flip(img, 0)  # Top - bottom.
    img = cv.flip(img, 1)  # Lefr - right.
    img = cv.flip(img, -1)  # Both of them.

    # Rotate.
    img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
    img = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)
    img = cv.rotate(img, cv.ROTATE_180)
    h, w, _ = img.shape

    # Affine transformation.
    matrix = cv.getRotationMatrix2D((w/2, h/2), 45, 0.5)  # (center, angle, scale)
    img = cv.warpAffine(img, matrix, (w, h))

    # Color.
    b, g, r = cv.split(img)
    r = r // 4
    img = cv.merge((b, g, r))
    img[:,:,0] = img[:,:,0] // 4
    # Grayscale.
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Binarization.
    #_, img = cv.threshold(img, 100, 255, cv.THRESH_BINARY)
    img = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
    # Invert.
    img = cv.bitwise_not(img)

    # Create border. (Add pixels)
    img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)  # Using BGR.
    color = [255, 0, 0]
    img = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_CONSTANT, value=color)


    return img


def draw(image):
    """
    (image, position, color, line)
    When line = -1, the diagram is filled.
    """

    img = image

    cv.line(img, (0, 0), (512, 512), (0, 0, 0), 3)
    cv.arrowedLine(img, (0, 512), (200, 300), (255, 255, 255), 3, tipLength=0.1)
    cv.rectangle(img, (200, 200), (300, 300), (0, 255, 0), 3)
    cv.circle(img, (250, 250), 50, (255, 0, 0), 3)
    cv.ellipse(img, (250, 250), (50, 25), 0, 0, 360, (0, 0, 255), 3)
    pts = np.array([[200, 220],
                    [200, 280],
                    [220, 300],
                    [280, 300],
                    [300, 280],
                    [300, 220],
                    [280, 200],
                    [220, 200],
                    ],
                    dtype=np.int32)
    pts = np.reshape(pts, (-1, 1, 2))
    cv.polylines(img, [pts], True, (255, 255, 255), 3)
    font = cv.FONT_HERSHEY_SIMPLEX
    size, _ = cv.getTextSize('TEXT', font, 1, 2)
    x = 250 - size[0]//2
    y = 250 + size[1]//2
    cv.putText(img, 'TEXT', (x, y), font, 1, (255, 255, 255), 2, cv.LINE_AA)


def mouse_event(image):
    """
    Draw circles on the image.
    Using global variables for callback functions.
    """

    global global_img
    global_img = image  # Reffer same object.

    cv.namedWindow('mouse_event')
    cv.setMouseCallback('mouse_event', callback)
    while True:
        cv.imshow('mouse_event', global_img)
        if cv.waitKey(20) & 0xFF == 27:  # Refresh images and wait [esc].
            break
    cv.destroyAllWindows()

    return global_img


def callback(event, x, y, flags, param):
    """
    Mouse callback function.
    Draw circles.
    """

    r = 15
    dx = round(r * math.cos(np.pi/4))
    dy = round(r * math.sin(np.pi/4))

    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(global_img, (x, y), r, (255, 255, 255), 3)
        cv.line(global_img, (x-dx, y-dy), (x+dx, y+dy), (255, 255, 255), 3)
        cv.line(global_img, (x+dx, y-dy), (x-dx, y+dy), (255, 255, 255), 3)


def trackbar(image):

    img = image
    img_orig = image.copy()
    color = np.empty_like(img_orig)
    cv.namedWindow('trackbar')
    cv.createTrackbar('B', 'trackbar', 0 ,255, nothing)
    cv.createTrackbar('G', 'trackbar', 0 ,255, nothing)
    cv.createTrackbar('R', 'trackbar', 0 ,255, nothing)

    while True:
        cv.imshow('trackbar', img)
        if cv.waitKey(20) & 0xFF == ord('q'):
            break
        b = cv.getTrackbarPos('B', 'trackbar')
        g = cv.getTrackbarPos('G', 'trackbar')
        r = cv.getTrackbarPos('R', 'trackbar')
        color[:] = [b, g, r]
        img = cv.add(img_orig, color)

    cv.destroyAllWindows()


def nothing(x):
    """
    Callback function.
    Don't do anything.
    """

    pass


def combine(image1, image2):
    """
    Replace: image2
    Add: image1 + image2(not masked)
    Marge: image1*P1 + image2*P2
    Superimpose: image1 + image2(masked)
    """

    img = image1
    img2 = image2

    # Resize image2.
    w = img.shape[1] // 2
    h = (img2.shape[0]*w) // img2.shape[1]  # h = H * w / W
    img2 = cv.resize(img2, (w, h))

    # Extruct image1.
    row, col, _ = img2.shape
    img1_sub = img[:row, :col]

    replace = img2
    add = cv.add(img1_sub, img2)
    marge = cv.addWeighted(img1_sub, 0.5, img2, 0.5, 0)

    mask = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    _, mask = cv.threshold(mask, 10, 255, cv.THRESH_BINARY)
    mask_inv = cv.bitwise_not(mask)
    img1_sub = cv.bitwise_and(img1_sub, img1_sub, mask=mask_inv)
    img2 = cv.bitwise_and(img2, img2, mask=mask)
    superimpose = cv.add(img1_sub, img2)

    # Select combine type.
    img[:row, :col] = superimpose

    return img


def video():
    """
    Use the built-in camera.
    Run this function by the original terminal.
    "a": Start recording.
    "q": Finish all.
    Please press and hold the above keys for a short time
    because the detecting speed is not fast.
    """

    cap = cv.VideoCapture(0)

    w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv.CAP_PROP_FPS)
    fourcc = cv.VideoWriter_fourcc('m', 'p', '4', 'v')
    out = cv.VideoWriter('output.mp4', fourcc, fps, (w, h))
    #fourcc = cv.VideoWriter_fourcc(*'XVID')
    #out = cv.VideoWriter('output.avi', fourcc, fps, (w, h))

    if not cap.isOpened():
        print('Cannot open camera.')
        sys.exit()

    font = cv.FONT_HERSHEY_SIMPLEX
    color = (255, 255, 255)
    flg = False
    while True:
        ret, frame = cap.read()
        if not ret:
            print('Cannot receive frame.')
            break
        #frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame = cv.flip(frame, 1)
        if cv.waitKey(1) == ord('a'):
            color = (0, 0, 255)
            flg = True
        cv.putText(frame, 'REC', (50, 100), font, 2, color, 3, cv.LINE_AA)
        cv.imshow('frame', frame)
        if flg:
            out.write(frame)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    out.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
