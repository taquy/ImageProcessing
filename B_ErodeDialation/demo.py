import cv2
import numpy as np
from matplotlib import pyplot as plt
import __init__ as app


def main():
	img = cv2.imread('../sample.jpg')
	# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	w = 300

	img = cv2.resize(img, (w, w), interpolation = cv2.INTER_CUBIC)

	labels = ['origin', 'erode', 'dialation', 'opening', 'closing', 'gradient', 'tophat', 'blackhat']
	images = []


	# MODULE TESTING
	# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	images.append(img)
	images.append(app.erode(img));
	images.append(app.dilate(img));
	images.append(app.opening(img));
	images.append(app.closing(img));
	images.append(app.gradient(img));
	images.append(app.tophat(img));
	images.append(app.blackhat(img));

	## END OF MODULE TESING

	h = 0
	v = 0
	for i in range(len(images)) :
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