import cv2 as cv
import numpy as np
img = cv.imread("images/10.png")
low_thre = 0
high_thre = 100
canny = cv.Canny(img,low_thre,high_thre)
cv.imshow("canny",canny)
cv.waitKey(0)
cv.destroyAllWindows()