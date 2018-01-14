"""
@file sobel_demo.py
@brief Sample code using Sobel and/or Scharr OpenCV functions to make a simple Edge Detector
"""
import sys
import cv2 as cv

# SOBEL
# doc: https://docs.opencv.org/master/d2/d2c/tutorial_sobel_derivatives.html
# dst =   cv.Sobel(   src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]] )
#
# (   InputArray  src,
# OutputArray     dst,
# int     ddepth,
# int     dx,
# int     dy,
# int     ksize = 3,
# double  scale = 1,
# double  delta = 0,
# int     borderType = BORDER_DEFAULT 
# )   

def sobel (ksize, wA = 0.5, wB = 0.5) :
    grad_x = cv.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    grad_y = cv.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    
    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)
    
    grad = cv.addWeighted(abs_grad_x, wA, abs_grad_y, wB, 0)

    return grad

# ADDWEIGHT
# doc: https://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html?highlight=addweighted#addweighted
# cv2.addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]]) → dst
# Parameters: 
# src1 – first input array.
# alpha – weight of the first array elements.
# src2 – second input array of the same size and channel number as src1.
# beta – weight of the second array elements.
# dst – output array that has the same size and number of channels as the input arrays.
# gamma – scalar added to each sum.
# dtype – optional depth of the output array; when both input arrays have the same depth, dtype can be set to -1, which will be equivalent to src1.depth().

def main():
    
    scale = 1
    delta = 0
    ddepth = cv.CV_16S
    
    src = cv.imread('sample.jpg')
    
    src = cv.GaussianBlur(src, (3, 3), 0)
    
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    
    grad_x = cv.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    grad_y = cv.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    
    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)
    
    grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    
    
    cv.imshow('demo', grad)
    cv.waitKey(0)
    return 0

if __name__ == "__main__":
    main()