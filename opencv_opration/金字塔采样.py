import cv2 as cv
import numpy as np
img1 = cv.imread("images/01.jpg")
img2 = cv.resize(img1,None,fx=0.5,fy=0.5)
#上采样
up_img = cv.pyrUp(img2)
down_img = cv.pyrDown(img2)
cv.imshow("before",img2)
cv.imshow("up",up_img)
cv.imshow("down",down_img)
cv.waitKey(0)
cv.destroyAllWindows()