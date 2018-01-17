import sys
import math
import cv2 as cv
import numpy as np

# HoughLines() and HoughLinesP() to detect lines in an image.
# Doc: 
# - https://docs.opencv.org/master/d9/db0/tutorial_hough_lines.html

# HoughLines(): https://docs.opencv.org/master/dd/d1a/group__imgproc__feature.html#ga46b4e588934f6c8dfd509cc6e0e4545a
# HoughLinesP(): https://docs.opencv.org/master/dd/d1a/group__imgproc__feature.html#ga8618180a5948286384e3b7ca02f6feeb

def houghProb(img) :
	return cv.HoughLinesP(img, 1, np.pi / 180, 50, None, 50, 10)


# 	lines	=	cv.HoughLines(	image, rho, theta, threshold[, lines[, srn[, stn[, min_theta[, max_theta]]]]]	)
# 	lines	=	cv.HoughLinesP(	image, rho, theta, threshold[, lines[, minLineLength[, maxLineGap]]]	)

# Parameters
# image				8-bit, single-channel binary source image. The image may be modified by the function.

# lines				Output vector of lines. Each line is represented by a two-element vector (ρ,θ) . ρ is the 							distance from the coordinate origin (0,0) (top-left corner of the image). θ is the line rotation 				     angle in radians ( 0∼vertical line,π/2∼horizontal line ).

# rho				Distance resolution of the accumulator in pixels.

# theta				Angle resolution of the accumulator in radians.

# threshold			Accumulator threshold parameter. Only those lines are returned that get enough votes ( >							𝚝𝚑𝚛𝚎𝚜𝚑𝚘𝚕𝚍 ).

# srn				For the multi-scale Hough transform, it is a divisor for the distance resolution rho . The coarse 					  accumulator distance resolution is rho and the accurate accumulator resolution is rho/srn . If 						both srn=0 and stn=0 , the classical Hough transform is used. Otherwise, both these parameters 						should be positive.

# stn				For the multi-scale Hough transform, it is a divisor for the distance resolution theta.

# min_theta	        For standard and multi-scale Hough transform, minimum angle to check for lines. Must fall between 					  0 and max_theta.

# max_theta			For standard and multi-scale Hough transform, maximum angle to check for lines. Must fall between 					  min_theta and CV_PI.

def hough(img) : # return lines
    return cv.HoughLines(img, 1, np.pi / 180, 150, None, 0, 0)
    

def demo(src):
    # Detect the edges
    dst = cv.Canny(src, 50, 200, None, 3)
    
    # Copy edges to the images that will display the results in BGR
    cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
    cdstP = np.copy(cdst)
    
    lines = cv.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)
    

    # draw lines
    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv.line(cdst, pt1, pt2, (0,0,255), 3, cv.LINE_AA)
    
    # draw lines
    linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)
    
    cv.imshow("Source", src)
    cv.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)
    cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdstP)
    
    cv.waitKey()
    return 0
    