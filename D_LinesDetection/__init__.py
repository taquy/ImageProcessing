"""
@file morph_lines_detection.py
@brief Use morphology transformations for extracting horizontal and vertical lines sample code
"""
import numpy as np
import sys
import cv2 as cv

# doc: https://docs.opencv.org/master/dd/dd7/tutorial_morph_lines_detection.html


def show_wait_destroy(winname, img):
    cv.imshow(winname, img)
    cv.moveWindow(winname, 500, 0)
    cv.waitKey(0)
    cv.destroyWindow(winname)


def main(argv):

    src = cv.imread('demo.png', cv.IMREAD_COLOR)
    if src is None: return -1

    # Show source image
    cv.imshow("src", src)
    # [load_image]
    # [gray]
    # Transform source image to gray if it is not already
    if len(src.shape) != 2:
        gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    else:
        gray = src


    # GRAY
    show_wait_destroy("GRAY", gray)

    # BIN
    gray = cv.bitwise_not(gray)
    bw = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                                cv.THRESH_BINARY, 15, -2)
    show_wait_destroy("BIN", bw)

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

    show_wait_destroy("horizontal", horizontal)



    # SPECIFY VERTICAL AXIS SIZE
    rows = vertical.shape[0]
    verticalsize = rows / 30

    # CREATING STRUCTURE ELEMENT
    verticalStructure = cv.getStructuringElement(cv.MORPH_RECT, (1, verticalsize))

    # MORPHOLOGY OPERATIONS
    vertical = cv.erode(vertical, verticalStructure)
    vertical = cv.dilate(vertical, verticalStructure)

    show_wait_destroy("vertical", vertical)




    # INVERSE VERTICAL IMAGE
    vertical = cv.bitwise_not(vertical)
    show_wait_destroy("INVERSE VERTICAL", vertical)


    '''
    Extract edges and smooth image according to the logic
    1. extract edges
    2. dilate(edges)
    3. src.copyTo(smooth)
    4. blur smooth img
    5. smooth.copyTo(src, edges)
    '''

    # Step 1
    edges = cv.adaptiveThreshold(vertical, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                                cv.THRESH_BINARY, 3, -2)
    show_wait_destroy("edges", edges)

    # Step 2
    kernel = np.ones((2, 2), np.uint8)
    edges = cv.dilate(edges, kernel)
    show_wait_destroy("dilate", edges)

    # Step 3
    smooth = np.copy(vertical)

    # Step 4
    smooth = cv.blur(smooth, (2, 2))

    # Step 5
    (rows, cols) = np.where(edges != 0)
    vertical[rows, cols] = smooth[rows, cols]

    show_wait_destroy("smooth - final", vertical)
    return 0

if __name__ == "__main__":
    main(sys.argv[1:])