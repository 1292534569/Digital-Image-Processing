import cv2 as cv
import numpy as np
img1 = cv.imread("images/01.jpg")
img2 = cv.resize(img1,None,fx=0.5,fy=0.5)
rows,cols = img2.shape[:2]
#需要4个点来创建变换矩阵
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[100,145],[300,100],[80,290],[310,300]])
T = cv.getPerspectiveTransform(pts1,pts2)
#实现变换
dst = cv.warpPerspective(img2,T,(rows,cols))
cv.imshow("before",img2)
cv.imshow("after",dst)
cv.waitKey(0)
cv.destroyAllWindows()