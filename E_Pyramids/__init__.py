
import cv2
import numpy as np

import sys

# Doc: https://docs.opencv.org/master/d4/d1f/tutorial_pyramids.html
#
# Use the OpenCV functions pyrUp() and pyrDown() to downsample or upsample a given image.

def bigger (img) :
	img = cv2.pyrUp(img, dstsize = (2 * cols, 2 * rows))
	return img

def smaller (img) :
	img = cv2.pyrDown(img, dstsize = (cols // 2, rows // 2))
	return img

def sample (img):
	print("""
	* [i] zoom in
	* [o] zoom out
	* [ESC] exit
	""")
	
	img = cv2.imread(filename)

	if img is None: return -1
	
	while 1:
		rows, cols, _channels = map(int, img.shape)
		cv2.imshow('Pyramids Demo', img)

		k = cv2.waitKey(0)
		if k == 27: break
		elif chr(k) == 'i':
			img = cv2.pyrUp(img, dstsize = (2 * cols, 2 * rows))
			print ('Zoom x2')
			
		elif chr(k) == 'o':
			img = cv2.pyrDown(img, dstsize = (cols // 2, rows // 2))
			print ('Zoom /2')
			
	cv2.destroyAllWindows()
	return 0