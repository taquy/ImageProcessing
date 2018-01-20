import cv2
import numpy as np
from matplotlib import pyplot as plt


def display(images, labels, rows = 2, cols = 2, fg = 1):
	plt.figure(fg)
	for i in xrange(len(images)) :
		images[i] = cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB)
		plt.subplot(rows , cols, i + 1),plt.imshow(images[i])
		plt.title(labels[i])
		plt.xticks([]),plt.yticks([])

def readMatrix(fp) :
	lines = list(fp)
	matrix = []
	for line in lines:
		line = line.replace('\n', '')
		line = line.split('\t')
		matrix.append(map(float, line))
	return matrix