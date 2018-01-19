import cv2
import numpy as np
from matplotlib import pyplot as plt
import __init__ as app


def main():
	img = cv2.imread('../sample.jpg')
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	w = 300

	img = cv2.resize(img, (w, w), interpolation = cv2.INTER_CUBIC)

	labels = ['origin', 'blur', 'median blur', 'bilateral blur', 'gaussian blur', 'box filter']
	images = []


	# MODULE TESTING


	## END OF MODULE TESING

	for i in range(len(images)) :
		plt.subplot(2,3,i + 1),plt.imshow(images[i])
		plt.title(labels[i])
		plt.xticks([]),plt.yticks([])
	
	plt.show()

	k = cv2.waitKey(0)
	# Esc key to stop
	if k==27: 
		cv2.destroyAllWindows()

if __name__== "__main__":
	main()