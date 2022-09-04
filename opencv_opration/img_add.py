import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img1 = cv.imread("images/05.jpg")
img2 = cv.imread("images/03-1.png")
img3 = cv.add(img1, img2)#cv_add
img4 = img1 + img2#numpy相加
cv.imshow("image",img3)
cv.imshow("image1",img4)
cv.waitKey(0)
cv.destroyWindow()