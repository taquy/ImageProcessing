import sys
from random import randint
import cv2 as cv

# doc: https://docs.opencv.org/master/dc/da3/tutorial_copyMakeBorder.html
# https://docs.opencv.org/master/d2/de8/group__core__array.html#ga2ac1049c2c3dd25c2b41bffe17658a36


def sample():
    
    borderType = cv.BORDER_CONSTANT
    
    # Loads an image
    src = cv.imread('sample.jpg', cv.IMREAD_COLOR)

    if src is None: return -1
    
    print ('\n'
           '\t   copyMakeBorder Demo: \n'
           '     -------------------- \n'
           ' ** Press \'c\' to set the border to a random constant value \n'
           ' ** Press \'r\' to set the border to be replicated \n'
           ' ** Press \'ESC\' to exit the program ')
    
    cv.namedWindow("result", cv.WINDOW_AUTOSIZE)
    
    top = int(0.05 * src.shape[0])  # shape[0] = rows
    bottom = top

    left = int(0.05 * src.shape[1])  # shape[1] = cols
    right = left
    
    while 1:
        
        value = [randint(0, 255), randint(0, 255), randint(0, 255)]
        
        dst = cv.copyMakeBorder(src, top, bottom, left, right, borderType, None, value)
        
        cv.imshow(window_name, dst)
        
        c = cv.waitKey(500)
        if c == 27: break
        elif c == 99: # 99 = ord('c')
            borderType = cv.BORDER_CONSTANT
        elif c == 114: # 114 = ord('r')
            borderType = cv.BORDER_REPLICATE
        
    return 0

if __name__ == "__main__":
    sample()