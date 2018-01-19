
import cv2
import numpy as np

import sys

# Doc: https://docs.opencv.org/master/d4/d1f/tutorial_pyramids.html
#
# Use the OpenCV functions pyrUp() and pyrDown() to downsample or upsample a given image.

def bigger (img, scale = 2) :
	return cv2.pyrUp(img, dstsize = (scale * cols, scale * rows))

def smaller (img, scale = 2) :
	return cv2.pyrDown(img, dstsize = (cols // scale, rows // scale))

