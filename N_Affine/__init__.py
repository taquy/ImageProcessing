import cv2
import numpy as np

# doc:
# - https://docs.opencv.org/master/d4/d61/tutorial_warp_affine.html


def scaling (img, scaleWidth, scaleHeight) :
	# interpolation methods are cv2.INTER_AREA for shrinking, cv2.INTER_CUBIC (slow), cv2.INTER_LINEAR for zooming. By default, interpolation method used is cv2.INTER_LINEAR for all resizing purposes.
	return cv2.resize(img, None, fx=scaleWidth, fy=scaleHeight, interpolation = cv2.INTER_CUBIC)


# translate:
# - param #1: image source
# - param #2: move horizontal
# - param #3: move vertical
# return: grayscale result
def translate (img, x, y) :
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	rows,cols = img.shape

	M = np.float32([[1,0,x],[0,1,y]])
	return cv2.warpAffine(img,M,(cols,rows))

# rotate:
# - param #1: image source
# - param #2: rotation angle
# return: grayscale result
def rotate (img, deg) :
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	rows, cols = img.shape

	M = cv2.getRotationMatrix2D((cols / 2, rows / 2), deg,1)
	return cv2.warpAffine(img,M,(cols,rows))

# rotataffineTransforme:
# - param #1: image source
# - param #2: triple roots points (source)
# - param #3: triple target points (destination)
# return: image result
def affineTransform (img, pts1, pts2) :
	rows, cols, ch = img.shape
	# pts1 = np.float32([[50,50],[200,50],[50,200]])
	# pts2 = np.float32([[10,100],[200,50],[100,250]])
	M = cv2.getAffineTransform(pts1,pts2)
	#doc: https://docs.opencv.org/2.4/modules/imgproc/doc/geometric_transformations.html?highlight=getaffinetransform
	return cv2.warpAffine(img,M,(cols,rows))
	#doc: https://docs.opencv.org/2.4/modules/imgproc/doc/geometric_transformations.html?highlight=getaffinetransform#void warpAffine(InputArray src, OutputArray dst, InputArray M, Size dsize, int flags, int borderMode, const Scalar& borderValue)

# rotataffineTransforme:
# - param #1: image source
# - param #2: 4 roots points (source)
# - param #3: 4 target points (destination)
# - param #4: a tuple of scaling
# return: image result
def perspective (img, pst1, pst2, scale) :
	rows,cols,ch = img.shape

	M = cv2.getPerspectiveTransform(pts1,pts2)

	return cv2.warpPerspective(img,M, scale)
