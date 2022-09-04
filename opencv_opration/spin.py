import imp


import cv2 as cv
import numpy as np
img1 = cv.imread("images/01.jpg")
img2 = cv.resize(img1,None,fx=0.5,fy=0.5)
rows,cols = img2.shape[:2]
#旋转矩阵M
M = cv.getRotationMatrix2D((cols/2,rows/2),90,0.4)
#旋转操作
dst = cv.warpAffine(img2,M,(rows,cols))
cv.imshow("initial",img2)
cv.imshow("rotate",dst)
cv.waitKey(0)
cv.destroyAllWindows()