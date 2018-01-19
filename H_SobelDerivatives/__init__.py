
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

def sobel (img, ksize = 5, ddepth = 5, scale = 5, delta = 5, wA = 0.5, wB = 0.5) :
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    grad_x = cv.Sobel(gray, ddepth, 1, 0, ksize, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    grad_y = cv.Sobel(gray, ddepth, 0, 1, ksize, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    
    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)
    
    grad = cv.addWeighted(abs_grad_x, wA, abs_grad_y, wB, 0)

    return grad

# ADDWEIGHT
# doc: https://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html?highlight=addweighted#addweighted
# cv2.addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]]) dst
# Parameters: 
# src1 - first input array.
# alpha - weight of the first array elements.
# src2 - second input array of the same size and channel number as src1.
# beta - weight of the second array elements.
# dst - output array that has the same size and number of channels as the input arrays.
# gamma - scalar added to each sum.
# dtype - optional depth of the output array; when both input arrays have the same depth, dtype can be set to -1, which will be equivalent to src1.depth().
