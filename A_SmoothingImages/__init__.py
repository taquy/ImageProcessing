import cv2
import numpy as np

# doc: https://docs.opencv.org/3.1.0/d4/d13/tutorial_py_filtering.html

def blur (img, kernel) :
	# dst = cv.blur( src, ksize[, dst[, anchor[, borderType]]] )

	# src	input image; it can have any number of channels, which are processed independently, but the depth should be CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.
	# dst	output image of the same size and type as src.
	# ksize	blurring kernel size.
	# anchor	anchor point; default value Point(-1,-1) means that the anchor is at the kernel center.
	# borderType	border mode used to extrapolate pixels outside of the image, see cv::BorderTypes

	return cv2.blur(img, (kernel, kernel))

def medianBlur (img, kernel) :
	# dst = cv.medianBlur( src, ksize[, dst] )

	# src: Source image
	# dst: Destination image, must be the same type as src
	# i: Size of the kernel (only one because we use a square window). Must be odd.

	return cv2.medianBlur(img, kernel)

def bilateralFilter (img, diameter, sigmaColor, sigmaSpace) :
	# dst	=	cv.bilateralFilter(	src, d, sigmaColor, sigmaSpace[, dst[, borderType]]	)

	# src: Source image
	# dst: Destination image
	# d: The diameter of each pixel neighborhood.
	# Color: Standard deviation in the color space.
	# Space: Standard deviation in the coordinate space (in pixel terms)

	return cv2.bilateralFilter(img, diameter, sigmaColor, sigmaSpace)


def gaussianBlur (img, kernel, sigmaX) :
	# dst	=	cv.GaussianBlur(	src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]	)
	
	# dst: Destination image
	# Size(w, h): The size of the kernel to be used (the neighbors to be considered). 
	# w and h have to be odd and positive numbers otherwise thi size will be calculated using the x and y arguments.

	# x: The standard deviation in x. Writing 0 implies that x is calculated using kernel size.
	# y: The standard deviation in y. Writing 0 implies that y is calculated using kernel size.

	return cv2.GaussianBlur(img, kernel, sigmaX)

def boxFilter (img, depth, kernel) :
	return cv2.boxFilter(img, depth, kernel)
