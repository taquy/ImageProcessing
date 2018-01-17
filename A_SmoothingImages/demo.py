import cv2
import numpy as np
import __init__ as app


def main():
	img = cv2.imread('../sample.jpg')
	cv2.imshow('img', img)
	cv2.waitKey(0)

if __name__== "__main__":
	main()