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
# import N_Affine as N
# import P_HistogramCalculation as P
import S_TemplateMatching as S

# def run() :
#
# 	img = cv2.imread('sample.jpg')
#
# 	P.drawHistogram(img)
#
# 	cv2.waitKey(0)
#
# run()

S.templateMatching(
	'./S_TemplateMatching/origin_1.jpg',
	'./S_TemplateMatching/template_1.png'
)