"""
@file morph_lines_detection.py
@brief Use morphology transformations for extracting horizontal and vertical lines sample code
"""
import numpy as np
import sys
import cv2 as cv

# doc: https://docs.opencv.org/master/dd/dd7/tutorial_morph_lines_detection.html


def extractLines(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # BIN
    gray = cv.bitwise_not(gray)
    bw = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                                cv.THRESH_BINARY, 15, -2)

    # EXTRACTING LINES
    horizontal = np.copy(bw)
    vertical = np.copy(bw)

    # SPECIFY HORIZONTAL AXIS SIZE
    cols = horizontal.shape[1]
    horizontal_size = cols / 30

    # CREATING STRUCTURE ELEMENT
    horizontalStructure = cv.getStructuringElement(cv.MORPH_RECT, (horizontal_size, 1))

    # MORPHOLOGY OPERATIONS
    horizontal = cv.erode(horizontal, horizontalStructure)
    horizontal = cv.dilate(horizontal, horizontalStructure)

    # SPECIFY VERTICAL AXIS SIZE
    rows = vertical.shape[0]
    verticalsize = rows / 30

    # CREATING STRUCTURE ELEMENT
    verticalStructure = cv.getStructuringElement(cv.MORPH_RECT, (1, verticalsize))

    # MORPHOLOGY OPERATIONS
    vertical = cv.erode(vertical, verticalStructure)
    vertical = cv.dilate(vertical, verticalStructure)


    # INVERSE VERTICAL IMAGE
    vertical = cv.bitwise_not(vertical)

    # Step 1
    edges = cv.adaptiveThreshold(vertical, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                                cv.THRESH_BINARY, 3, -2)

    # Step 2
    kernel = np.ones((2, 2), np.uint8)
    edges = cv.dilate(edges, kernel)

    # Step 3
    smooth = np.copy(vertical)

    # Step 4
    smooth = cv.blur(smooth, (2, 2))

    # Step 5
    (rows, cols) = np.where(edges != 0)
    vertical[rows, cols] = smooth[rows, cols]

    return vertical, horizontal;