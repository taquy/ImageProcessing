import numpy as np
import cv2

img = cv2.imread('noise.jpg', cv2.IMREAD_GRAYSCALE)

height = img.shape[0]
width = img.shape[1]

weights = np.array(
    [
        [0, 1, 1, 1, 0],
        [1, 2, 2, 2, 1],
        [1, 1, 5, 1, 1],
        [1, 2, 2, 2, 1],
        [0, 2, 2, 2, 1]
    ])

filter_size = weights.shape[0]
border_min = int(filter_size / 2)
border_max = border_min + filter_size%2

M = int((sum(sum(weights)) - 1) / 2)

for i in np.arange(border_min, height-border_min):
    for j in np.arange(border_min, width-border_min):
        neighbors = []

        for k in np.arange(- border_min,border_max):
            for l in np.arange(- border_min,border_max):
                a = img.item(i + k, j + l)
                w = weights[k, l]
                for _ in np.arange(w):
                    neighbors.append(a)
        neighbors.sort()
        median = neighbors[M]
        b = median
        img.itemset((i, j), b)


cv2.imshow('blur', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
