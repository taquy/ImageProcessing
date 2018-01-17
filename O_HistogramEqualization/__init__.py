import cv2
import numpy as np

# Doc: https://docs.opencv.org/master/d4/d1b/tutorial_histogram_equalization.html
#
# What is an Image Histogram?
# graphical representation of the intensity distribution of an image.
# quantifies the number of pixels for EACH intensity value considered.

# What is Histogram Equalization?
# method that improves the contrast in an image, stretch out the intensity range.
def histogram(img) :
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	return cv2.equalizeHist(img)