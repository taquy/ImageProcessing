import cv2
import numpy as np
from matplotlib import pyplot as plt
import __init__ as app


def main():
	img = cv2.imread('../sample.jpg')
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	w = 300

	img = cv2.resize(img, (w, w), interpolation = cv2.INTER_CUBIC)

	labels = ['THRESH_BINARY', 'THRESH_BINARY_INV', 'THRESH_TRUNC'
		, 'THRESH_TOZERO', 'THRESH_TOZERO_INV']
	images = []


	# MODULE TESTING
	images.append(app.translate(img))
	images.append(app.rotate(img))
	images.append(app.affineTransform(img))
	images.append(app.perspective(img))
	## END OF MODULE TESING

	for i in xrange(len(images)) :
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