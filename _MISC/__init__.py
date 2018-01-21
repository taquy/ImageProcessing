import cv2
import numpy as np

# COLOR SPACES : https://www.learnopencv.com/color-spaces-in-opencv-cpp-python/
def gray (img) :
	return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def hsv (img) :
	return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def lab (img) :
	return cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

def ycb (img) :
	return cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)


# filter: 
# inrange: lowerhsv + upperhsv
def filter (img, lower, upper) :
	img = hsv(img)
	return cv2.inRange(img, lower, upper)

# combine / image blending: https://docs.opencv.org/3.2.0/d0/d86/tutorial_py_image_arithmetics.html
# addWeight: image1, opacity1, image2, opacity2
def combine (img1, img2, o1 = 0.5, o2 = 0.5) :
	return cv2.addWeighted(img1, o1, img2, o2, 0)


# BITWISE OPERATOR
# doc: https://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html
def bitand (img1, img2) :
	return cv2.bitwise_and(img1, img2)

def bitnot (img1, img2) :
	return cv2.bitwise_not(img1, img2)

def bitor (img1, img2) :
	return cv2.bitwise_or(img1, img2)

def bitxor (img1, img2) :
	return cv2.bitwise_xor(img1, img2)

