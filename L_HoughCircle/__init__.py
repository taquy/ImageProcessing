import sys
import cv2 as cv
import numpy as np

# doc: https://docs.opencv.org/master/dd/d1a/group__imgproc__feature.html#ga47849c3be0d0406ad3ca45db65a25d2d
# - https://docs.opencv.org/master/d4/d70/tutorial_hough_circle.html

#   circles =   cv.HoughCircles(    image, method, dp, minDist[, circles[, param1[, param2[, minRadius[, maxRadius]]]]] )
#


# image   8-bit, single-channel, grayscale input image.

# circles [(x,y,radius), ..]

# method  Detection method, only HOUGH_GRADIENT

# dp  Inverse ratio of the accumulator resolution to the image resolution. For example, if dp=1 , the accumulator has the same resolution as the input image. If dp=2 , the accumulator has half as big width and height.

# minDist Minimum distance between the centers of the detected circles. If the parameter is too small, multiple neighbor circles may be falsely detected in addition to a true one. If it is too large, some circles may be missed.

# param1  First method-specific parameter. In case of CV_HOUGH_GRADIENT , it is the higher threshold of the two passed to the Canny edge detector (the lower one is twice smaller).

# param2  accumulator threshold for the circle centers at the detection stage. The smaller, the more false circles may be detected. Circles, corresponding to the larger accumulator values, will be returned first.

# minRadius   Minimum circle radius.

# maxRadius   Maximum circle radius. If <= 0, uses the maximum image dimension. If < 0, returns centers without finding the radius.

def hough(img) :
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 5)
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8, param1=100, param2=30, minRadius=1, maxRadius=30)

def demo(src):
    
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    
    gray = cv.medianBlur(gray, 5)
    
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8, param1=100, param2=30, minRadius=1, maxRadius=30)
    
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv.circle(src, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv.circle(src, center, radius, (255, 0, 255), 3)
    
    cv.imshow("detected circles", src)
    cv.waitKey(0)
    
    return 0