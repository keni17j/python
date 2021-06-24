"""
Pillow.
"""

import os
import sys

import numpy as np
from PIL import Image
from PIL import ImageOps, ImageChops, ImageFilter


def main():

    # Select an image/
    file_path = input('file path -> ')
    #file_path = r'the image file path'
    img = Image.open(file_path)
    print('format :', img.format,
          '\n' 'size :', img.size,
          '\n' 'mode :', img.mode,
          )

    img = edit(img)

    # Show.
    img.show()

    # Save
    #img.save(test.jpg)


def edit(image):

    img = image

    # Convert modes.
    """
    L: 8 bits, grayscale
    RGB: 8 bits x 3
    RGBA: 8 bits x 4 (alpha)
    CMYK: 8 bits x 4
    etc...
    """
    img = img.convert('L')

    # Rotate.
    img = img.rotate(45, expand=True)
    img = ImageOps.mirror(img)
    img = ImageOps.flip(img)
    # Resize.
    img = img.resize((100, 100))
    #img.thumbnail((100,100))  # Keep the aspect ratios.
    # Crop.
    img = img.crop((30, 30, 60, 60))  # (left, upper, right, lower)
    # Offset.
    img = ImageChops.offset(img, 10, 10)  # (image, x, y)

    # Filter.
    """
    FIND_EDGES
    CONTOUR
    BLUR
    GaussianBlur(radius=5)
    etc...
    """
    img = img.filter(ImageFilter.GaussianBlur(radius=5))

    # Binarization with numpy.
    img = img.convert('L')  # Grayscale.
    img = np.array(img)  # Convert to ndarray from PIL.
    thr = np.mean(img)  # Threshold.
    #img = (img>thr) * 255  # The simplest way.
    img[img<=thr] = 0  # Black.
    img[img>thr] = 255  # White.
    img = Image.fromarray(img.astype(np.uint8)) # Convert to PIL from ndarray.

    return img


if __name__ == '__main__':
    main()
