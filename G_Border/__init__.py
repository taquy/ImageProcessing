import sys
from random import randint
import cv2 as cv

# doc: https://docs.opencv.org/master/dc/da3/tutorial_copyMakeBorder.html
# https://docs.opencv.org/master/d2/de8/group__core__array.html#ga2ac1049c2c3dd25c2b41bffe17658a36


def border(img, brgVal):
    
    borderType = cv.BORDER_CONSTANT
    
    top = int(0.05 * img.shape[0])  # shape[0] = rows
    bottom = top

    left = int(0.05 * img.shape[1])  # shape[1] = cols
    right = left
    
    return cv.copyMakeBorder(img, top, bottom, left, right, borderType, None, brgVal)
