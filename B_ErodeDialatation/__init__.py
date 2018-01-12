import cv2
import numpy as np

def erode (img, kernel = 5, iterations = 1) :
	kernel = np.ones((kernel, kernel), np.uint8)
	result = cv2.erode(img, kernel, iterations = 1)
	return result

def dialation (img, kernel = 5, iterations = 1) :
	result = cv2.dilate(img, kernel, iterations)
	return result

def opening (img, kernel = 5) :
	result = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
	return result

def closing (img, kernel = 5) :
	result = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
	return result

def gradient (img, kernel = 5) :
	result = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
	return result

def tophat (img, kernel = 5) :
	result = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
	return result

def blackhat (img, kernel = 5) :
	result = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
	return result
	