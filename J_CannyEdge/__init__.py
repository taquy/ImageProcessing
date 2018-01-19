import cv2
import numpy as np

# doc:
# - https://docs.opencv.org/master/da/d5c/tutorial_canny_detector.html
# - https://docs.opencv.org/3.3.1/da/d22/tutorial_py_canny.html
# - https://docs.opencv.org/3.3.1/dd/d1a/group__imgproc__feature.html#ga04723e007ed888ddf11d9ba04e2232de
#

# The function finds edges in the input image image and marks them in the output map edges using the Canny algorithm. The smallest value between threshold1 and threshold2 is used for edge linking

# void cv::Canny	(	InputArray 	image,
# 	OutputArray 	edges,
# 	double 	threshold1,
# 	double 	threshold2,
# 	int 	apertureSize = 3,
# 	bool 	L2gradient = false 
# )		
#
# image	8-bit input image.
# edges	output edge map; single channels 8-bit image, which has the same size as image .
# threshold1	first threshold for the hysteresis procedure.
# threshold2	second threshold for the hysteresis procedure.
# apertureSize	aperture size for the Sobel operator.
# L2gradient	a flag, indicating whether a more accurate

def canny(img, thres1 = 125, thres2 = 255) :
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	return cv2.Canny(gray, thres1, thres2)