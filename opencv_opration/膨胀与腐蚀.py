import cv2 as cv
import numpy as np
img = cv.imread("images/06.png")
#创建内核
kernel = np.ones((5,5),np.uint8)
erosin = cv.erode(img, kernel)
dilate = cv.dilate(img, kernel)
cv.imshow("before",img)
cv.imshow("eros",erosin)
cv.imshow("dile",dilate)
cv.waitKey(0)
cv.destroyAllWindows()
