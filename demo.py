import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

import A_SmoothingImages as A
import B_ErodeDialation as B
import C_HitMiss as C
import D_LinesDetection as D
import E_Pyramids as E
import F_Thresholding as F
import G_Border as G
import H_SobelDerivatives as H
import I_Laplace as I
import J_CannyEdge as J
import K_HoughLine as K
import L_HoughCircle as L 
import N_Affine as N
import O_HistogramEqualization as O
import P_HistogramCalculation as P
import Q_HistogramComparison as Q
import S_TemplateMatching as S
import T_FindContour as T

import _IO as io
from _IO import VideoReader
import _MATRIX as mat
import _GRAPH as graph
import _MISC as misc



def work1 () :
	labels = ['board.png', 'sinusoidal.png']
	images = [
		cv2.imread('_sampletest/exam1/board.png'),
		cv2.imread('_sampletest/exam1/sinusoidal.png')
	]
	io.display(images, labels, 1)

def work2() :
	ci = io.readMatrix(open('_sampletest/exam1/CI.txt'))
	cj = io.readMatrix(open('_sampletest/exam1/CJ.txt'))
	ci = np.asarray(ci)
	cj = np.asarray(cj)

	m = len(ci)

	UxI = 0
	UxJ = 0

	UyI = 0
	UyJ = 0

	OxI = 0
	OxJ = 0

	OyI = 0
	OyJ = 0

	for j in range (1, m + 1) :
		UxI += j * sum (ci[j - 1])
		UxJ += j * sum (cj[j - 1])
		UyI += j * mat.sumCol(ci, j - 1)
		UyJ += j * mat.sumCol(cj, j - 1)

	for j in range (1, m + 1) :
		OxI += math.pow((j - UxI), 2) *  sum (ci[j - 1])
		OxJ += math.pow((j - UxJ), 2) *  sum (cj[j - 1])
		OyI += math.pow((j - UyI), 2) *  mat.sumCol (ci, j - 1)
		OyJ += math.pow((j - UyJ), 2) *  mat.sumCol (cj, j - 1)

	OxI = math.sqrt(OxI)
	OxJ = math.sqrt(OxJ)

	OyI = math.sqrt(OyI)
	OyJ = math.sqrt(OyJ)

	A = [UxI, UyI, OxI, OyI]
	B = [UxJ, UyJ, OxJ, OyJ]
	
	graph.bar(4, A, B)

	return A, B, ci, cj

def work3(A, B, ci, cj):
	x1 = [0, 0]
	x2 = [0, 0]
	x3 = [0, 0]

	for i in range (1, len(ci) + 1) :
		for j in range (1, len(ci) + 1) :
			x1[0] += math.pow(ci[i - 1][j - 1], 2)
			x1[1] += math.pow(cj[i - 1][j - 1], 2)

			x2[0] += math.pow(i - j, 2) * ci[i - 1][j - 1]
			x2[1] += math.pow(i - j, 2) * cj[i - 1][j - 1]

			x3[0] += ((i - A[0]) * (j - A[1]) * ci[i - 1][j - 1]) / (A[2] * A[3])
			x3[1] += ((i - B[0]) * (j - B[1]) * cj[i - 1][j - 1]) / (B[2] * B[3])

	Ys = [
		[x1[0], x2[0], x3[0]],
		[x1[1], x2[1], x3[1]]
	]
	graph.line([1,2,3], Ys, 3)


if __name__== '__main__':
	reader = VideoReader(path='sample.webm', size=(1920, 1080), out_path='test_out.mp4')
	reader.display()
	print(reader.fps)
	# work1()
	# A, B, ci, cj = work2()
	# work2()
	# work3(A, B, ci, cj)
	# plt.show()














# S.templateMatching(
# 	'./S_TemplateMatching/origin_1.jpg',
# 	'./S_TemplateMatching/template_1.png'
# )

# img = T.findContours('sample.jpg')
# cv2.namedWindow('Result', cv2.WINDOW_AUTOSIZE)
# cv2.imshow('Result', img)
# cv2.waitKey(0)