import sys
import math
import cv2 as cv
import numpy as np

# HoughLines() and HoughLinesP() to detect lines in an image.
# Doc: 
# - https://docs.opencv.org/master/d9/db0/tutorial_hough_lines.html

# HoughLines(): https://docs.opencv.org/master/dd/d1a/group__imgproc__feature.html#ga46b4e588934f6c8dfd509cc6e0e4545a
# HoughLinesP(): https://docs.opencv.org/master/dd/d1a/group__imgproc__feature.html#ga8618180a5948286384e3b7ca02f6feeb

def houghProb(img) :
	return cv.HoughLinesP(img, 1, np.pi / 180, 50, None, 50, 10)


# 	lines	=	cv.HoughLines(	image, rho, theta, threshold[, lines[, srn[, stn[, min_theta[, max_theta]]]]]	)
# 	lines	=	cv.HoughLinesP(	image, rho, theta, threshold[, lines[, minLineLength[, maxLineGap]]]	)

# Parameters
# image				8-bit, single-channel binary source image. The image may be modified by the function.

# lines				Output vector of lines. 

# rho				Distance resolution of the accumulator in pixels.

# theta				Angle resolution of the accumulator in radians.

# threshold			Accumulator threshold parameter. Only those lines are returned that get enough votes .

# srn				For the multi-scale Hough transform, it is a divisor for the distance resolution rho . The coarse 					  accumulator distance resolution is rho and the accurate accumulator resolution is rho/srn . If 						both srn=0 and stn=0 , the classical Hough transform is used. Otherwise, both these parameters 						should be positive.

# stn				For the multi-scale Hough transform, it is a divisor for the distance resolution theta.

# min_theta	        For standard and multi-scale Hough transform, minimum angle to check for lines. Must fall between 					  0 and max_theta.

# max_theta			For standard and multi-scale Hough transform, maximum angle to check for lines. Must fall between 					  min_theta and CV_PI.

def hough(img) : # return lines
    return cv.HoughLines(img, 1, np.pi / 180, 150, None, 0, 0)
    