import cv2
import numpy as np
from matplotlib import pyplot as plt
import __init__ as app


def main():
	img = cv2.imread('../sample.jpg')
	# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	w = 300

	img = cv2.resize(img, (w, w), interpolation = cv2.INTER_CUBIC)

	labels = ['origin', 'blur', 'median blur', 'bilateral blur', 'gaussian blur', 'box filter']
	images = []


	# MODULE TESTING
	images.append(img)
	images.append(app.blur(img, 15))
	images.append(app.medianBlur(img, 15))
	images.append(app.bilateralFilter(img, 15, 90, 90))
	images.append(app.gaussianBlur(img, (15, 15), 0))
	# images.append(app.boxFilter(img, 3, 7))

	## END OF MODULE TESING

	h = 0
	v = 0
	for i in xrange(len(images)) :
		cv2.namedWindow(labels[i]);

		x =  (w + 20) * h
		y = (w + 50) * v

		h = h + 1
		if h == 4: 
			h = 0
			v = v + 1

		cv2.moveWindow(labels[i], x, y);
		cv2.imshow(labels[i], images[i])

	# plt.subplot(1,2,1),plt.imshow(app.blur(img, 15))
	# plt.title(labels[0])
	# plt.xticks([]),plt.yticks([])
	# plt.show()

	k = cv2.waitKey(0)
	# Esc key to stop
	if k==27: 
		cv2.destroyAllWindows()

if __name__== "__main__":
	main()