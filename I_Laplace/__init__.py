import sys
import cv2 as cv

# LAPLACE
# doc: https://docs.opencv.org/master/d5/db5/tutorial_laplace_operator.html
#
# dst = cv.Laplacian(src_gray, ddepth, kernel_size)
#
# PARAMETERS: 
# src_gray: The input image.
# dst: Destination (output) image
# ddepth: Depth of the destination image. Since our input is CV_8U we define ddepth = CV_16S to avoid overflow
# kernel_size: The kernel size of the Sobel operator to be applied internally. We use 3 in this example.
# scale, delta and BORDER_DEFAULT: We leave them as default values.

def laplace(img, ksize = 3):

    ddepth = cv.CV_16S

    img = cv.GaussianBlur(img, (3, 3), 0)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    dst = cv.Laplacian(gray, ddepth, ksize)

    return cv.convertScaleAbs(dst)