# doc
# https://docs.opencv.org/3.0-beta/modules/imgproc/doc/histograms.html


# USAGE
# python compare.py --dataset images

# import the necessary packages
from scipy.spatial import distance as dist
import matplotlib.pyplot as plt
import numpy as np
import argparse
import glob
import cv2

# store image label (filename) to dictionary
labels = {}
# store image data to array
images = []

for path in glob.glob("images/*.png"):
	filename = path[path.rfind("/") + 1:]
	image = cv2.imread(path)
	images.append(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

	# extract a 3D RGB color histogram, use 8 bins/channel, normalize,
	hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
	hist = cv2.normalize(hist, image).flatten()
	labels[filename] = hist


	# NORMALIZE
OPENCV_METHODS = (
	("Correlation", cv2.HISTCMP_CORREL),
	("Chi-Squared", cv2.HISTCMP_CHISQR),
	("Intersection", cv2.HISTCMP_INTERSECT), 
	("Hellinger", cv2.HISTCMP_BHATTACHARYYA))

# loop over the comparison methods
for (methodName, method) in OPENCV_METHODS:
	results = {}
	reverse = False

	# reverse results if using method correlation / intersection
	if methodName in ("Correlation", "Intersection"): reverse = True

	# compare histogram
	for (k, hist) in labels.items():
		d = cv2.compareHist(labels["doge.png"], hist, method)
		results[k] = d

	# sort results
	results = sorted([(v, k) for (k, v) in results.items()], reverse = reverse)


	## DISPLAY RESULTS
	fig = plt.figure("Query")
	ax = fig.add_subplot(1, 1, 1)
	ax.imshow(images[0])
	plt.axis("off")

	# initialize the results figure
	fig = plt.figure("Results: %s" % (methodName))
	fig.suptitle(methodName, fontsize = 10)

	for (i, (v, k)) in enumerate(results):
		# show the result
		ax = fig.add_subplot(3, len(images) / 2, i + 1)
		ax.set_title("%s: %.2f" % (k, v))
		plt.imshow(images[i])
		plt.axis("off")

# show the OpenCV methods
plt.show()