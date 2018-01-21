import numpy as np
import cv2
# doc : https://docs.opencv.org/master/d1/da0/tutorial_remap.html
# - 

# REMAPPING
# the process of taking pixels from one place in the image and locating them in another position in a new image.

def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")

    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    return rect

def draw_Rect_cover(image,rect):
    (tl, tr, br, bl) = rect

    a = (int(tl[0]), int(tl[1]))
    b = (int(tr[0]), int(tr[1]))
    c = (int(br[0]), int(br[1]))
    d = (int(bl[0]), int(bl[1]))

    cv2.line(image, a, b, [0, 255, 0], 2)
    cv2.line(image, b, c, [0, 255, 0], 2)
    cv2.line(image, c, d, [0, 255, 0], 2)
    cv2.line(image, d,a, [0, 255, 0], 2)
    return image

def four_point_transform(image, pts):
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    draw_Rect_cover(image,rect)
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    # return the warped image
    return warped


# image = cv2.imread('cap.jpg')
# #pts = np.array([(324, 256), (478, 288), (478, 650), (336, 764)])#selected point
# pts = np.array([(0, 250), (636, 250), (600, 475), (36, 475)])#selected point

# warped = four_point_transform(image, pts)

# cv2.imshow("Original", image)
# cv2.imshow("Warped", warped)
# cv2.waitKey(0)