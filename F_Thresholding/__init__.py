import cv2 as cv2
import numpy as np

# doc: https://docs.opencv.org/3.3.1/d7/d4d/tutorial_py_thresholding.html

def tbin(img, value, maxbinval) :
	ret, result = cv2.threshold(img, value, maxbinval,cv2.THRESH_BINARY)
	return result

def tbinInverted(img, value, maxbinval) :
	ret, result = cv2.threshold(img, value, maxbinval,cv2.THRESH_BINARY_INV)
	return result

def tbinTruncate(img, value, maxbinval) :
	ret, result = cv2.threshold(img, value, maxbinval,cv2.THRESH_TRUNC)
	return result

def tbinToZero(img, value, maxbinval) :
	ret, result = cv2.threshold(img, value, maxbinval,cv2.THRESH_TOZERO)
	return result

def tbinToZeroInverted(img, value, maxbinval) :
	ret, result = cv2.threshold(img, value, maxbinval,cv2.THRESH_TOZERO_INV)
	return result

