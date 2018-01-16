import cv2
import numpy as np
from matplotlib import pyplot as plt

# doc: 
# https://docs.opencv.org/master/d8/dbc/tutorial_histogram_calculation.html
#	- python: https://docs.opencv.org/3.3.1/d1/db7/tutorial_py_histogram_begins.html

def drawHistogram(img) :
	color = ('b','g','r')

	for i,col in enumerate(color):
	    histr = cv2.calcHist([img],[i],None,[256],[0,256])
	    plt.plot(histr,color = col)
	    plt.xlim([0,256])

	plt.show()