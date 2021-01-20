import numpy
import cv2

im_g = cv2.imread("smallgray.png", 0)

print(im_g)

im_bgr = cv2.imread("smallgray.png", 1)

print(im_bgr)

cv2.imwrite("newsmallgray.png", im_g)