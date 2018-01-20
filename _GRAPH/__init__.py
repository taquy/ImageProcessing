# Credit: Josh Hemann

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple


def bar (n_groups, A, B) :
	# n_groups = 4
	# print A
	# print B

	# A = (90, 55, 40, 65)
	# B = (85, 62, 54, 20)
	# print A
	# print B
	# return
	# create plot
	fig, ax = plt.subplots()
	index = np.arange(n_groups)
	bar_width = 0.35
	 
	rects1 = plt.bar(index, A, bar_width, color='b')
	rects2 = plt.bar(index + bar_width, B, bar_width, color='g')
	 
	plt.xticks(index + bar_width / 2, ('A', 'B', 'C', 'D'))
	 
	plt.tight_layout()
	plt.show()

def line (X, Ys) :

	# X = [1,2,3,4,5,6]
	# Y = [2,5,4,3,7,9]
	# Y2 = [1,3,1,2,3,9]
	for Y in Ys :
		plt.plot(X, Y)

	plt.show()