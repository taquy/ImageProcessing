import cv2
import numpy as numpy
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
import _MATRIX as mat
import _GRAPH as graph



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

	# calculate Ux
	Ux = [0, 0]
	Uy = [0, 0]
	Ox = [0, 0]
	Oy = [0, 0]

	for j in range (1, len(ci)) :
		Ux[0] += j * sum(ci[j])
		Uy[0] += j * mat.sumCol(ci, j)
		Ox[0] += math.pow(j - Ux[0], 2) * sum(ci[j])
		Oy[0] += math.pow(j - Uy[0], 2) * mat.sumCol(ci, j)

	Ox[0] = math.sqrt(Ox[0])
	Oy[0] = math.sqrt(Oy[0])

	for j in range (1, len(cj)) :
		Ux[1] += j * sum(cj[j])
		Uy[1] += j * mat.sumCol(cj, j)
		Ox[1] += math.pow(j - Ux[1], 2) * sum(cj[j])
		Oy[1] += math.pow(j - Uy[1], 2) * mat.sumCol(cj, j)

	Ox[1] = math.sqrt(Ox[1])
	Oy[1] = math.sqrt(Oy[1])

	groupA = (Ux[0], Uy[0], Ox[0], Oy[0])
	groupB = (Ux[1], Uy[1], Ox[1], Oy[1])
	graph.bar(4, groupA, groupB, 1)

	return groupA, groupB, ci, cj

def work3(A, B, ci, cj):
	x1 = [0, 0]
	x2 = [0, 0]
	x3 = [0, 0]

	for i in range (1, len(ci)) :
		for j in range (1, len(ci)) :
			x1[0] += math.pow(ci[i][j], 2)
			x1[1] += math.pow(cj[i][j], 2)

			x2[0] += math.pow(i - j, 2) * ci[i][j]
			x2[1] += math.pow(i - j, 2) * cj[i][j]

			x3[0] += ((i - A[0]) * (i - A[1]) * ci[i][j]) / (A[2] * A[3])
			x3[1] += ((i - B[0]) * (i - B[1]) * cj[i][j]) / (B[2] * B[3])

	Ys = [
		[x1[0], x2[0], x3[0]],
		[x1[1], x2[1], x3[1]]
	]
	graph.line([1,2,3], Ys, 3)


if __name__== '__main__':
	work1()
	A, B, ci, cj = work2()
	work3(A, B, ci, cj)
	plt.show()














# S.templateMatching(
# 	'./S_TemplateMatching/origin_1.jpg',
# 	'./S_TemplateMatching/template_1.png'
# )

# img = T.findContours('sample.jpg')
# cv2.namedWindow('Result', cv2.WINDOW_AUTOSIZE)
# cv2.imshow('Result', img)
# cv2.waitKey(0)