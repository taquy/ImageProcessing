import cv2
import numpy as numpy
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

if __name__== '__main__':
	labels = ['board.png', 'sinusoidal.png']
	images = [
		cv2.imread('_sampletest/exam1/board.png'),
		cv2.imread('_sampletest/exam1/sinusoidal.png')
	]

	io.display(images, labels)
















# S.templateMatching(
# 	'./S_TemplateMatching/origin_1.jpg',
# 	'./S_TemplateMatching/template_1.png'
# )

# img = T.findContours('sample.jpg')
# cv2.namedWindow('Result', cv2.WINDOW_AUTOSIZE)
# cv2.imshow('Result', img)
# cv2.waitKey(0)