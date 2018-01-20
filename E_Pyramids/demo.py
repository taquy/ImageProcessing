
import cv2
import numpy as np

import sys

def demo (img):
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

demo(cv2.imread('../sample.jpg'))