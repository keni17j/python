import sys
import os
import numpy as np
from PIL import Image
from PIL import ImageOps, ImageChops, ImageFilter


def main():

    # select an image
    file_path = input("the image file path -> ")
    #file_path = r"the image file path"
    img = Image.open(file_path)
    print("format :", img.format,
          "\n", "size :", img.size,
          "\n", "mode :", img.mode)

    # convert modes
    """
    L: 8 bits, grayscale
    RGB: 8 bits x 3
    RGBA: 8 bits x 4 (alpha)
    CMYK: 8 bits x 4
    etc...
    """
    img = img.convert("L")

    # rotate
    img = img.rotate(45, expand=True)
    img = ImageOps.mirror(img)
    img = ImageOps.flip(img)

    # resize
    img = img.resize((100, 100))
    #img.thumbnail((100,100)) # keep the aspect ratios

    # crop
    img = img.crop((30,30, 60,60))

    # offset
    img = ImageChops.offset(img, 10,10)

    # filter
    """
    FIND_EDGES
    CONTOUR
    BLUR
    GaussianBlur(radius=5)
    etc...
    """
    img = img.filter(ImageFilter.GaussianBlur(radius=5))

    # binaryzation with numpy
    img = img.convert("L") # grayscale
    img = np.array(img) # to ndarray from PIL
    thr = np.mean(img) # threshold
    img[img<=thr] = 0 # black
    img[img>thr] = 255 # white
    img = Image.fromarray(img.astype(np.uint8)) # to PIL from ndarray

    # show
    img.show()

    # save
    """
    file_name = "test.jpg"
    img.save(file_name)
    """



if __name__ == "__main__": main()
