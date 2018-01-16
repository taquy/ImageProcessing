import cv2
import numpy as numpy
# import A_SmoothingImages as A
# import B_ErodeDialation as B
# import C_HitMiss as C
# import D_LinesDetection as D
# import E_Pyramids as E
# import F_Thresholding as F
# import G_Border as G
# import H_SobelDerivatives as H
# import I_Laplace as I
# import J_CannyEdge as J
# import K_HoughLine as K
# import L_HoughCircle as L 
# import M_Remapping as M
import N_HistogramEqualization as N

def run() :

	img = cv2.imread('sample.jpg')
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	result = N.histogram(gray)

	cv2.imshow('result', result)
	cv2.waitKey(0)

run()