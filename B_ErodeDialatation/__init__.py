import cv2
import numpy as np

def erode (img, kernel = 5, iterations = 1) :
	kernel = np.ones((kernel, kernel), np.uint8)
	result = cv2.erode(img, kernel, iterations = 1)
	return result

def dilate (img, kernel = 5, iterations = 1) :
	result = cv2.dilate(img, (kernel, kernel), iterations)
	return result

def opening (img, kernel = 5) :
	result = cv2.morphologyEx(img, cv2.MORPH_OPEN, (kernel, kernel))
	return result

def closing (img, kernel = 5) :
	result = cv2.morphologyEx(img, cv2.MORPH_CLOSE, (kernel, kernel))
	return result

def gradient (img, kernel = 5) :
	result = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, (kernel, kernel))
	return result

def tophat (img, kernel = 5) :
	result = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, (kernel, kernel))
	return result

def blackhat (img, kernel = 5) :
	result = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, (kernel, kernel))
	return result
	