import cv2
import numpy as np

# Video: https://www.youtube.com/watch?v=vWWpZtQxlzA
# Doc: https://docs.opencv.org/master/db/d06/tutorial_hitOrMiss.html
#
#

def hitmiss(img, kernel) :
    output_image = cv2.morphologyEx(img, cv2.MORPH_HITMISS, kernel)
    return output_image

