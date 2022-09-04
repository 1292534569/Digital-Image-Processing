import cv2 as cv
import numpy as np
img1 = cv.imread("images/01.jpg")
img2 = cv.resize(img1,None,fx=0.5,fy=0.5)
rows,cols = img2.shape[:2]
#确定变换前后的三个点以解出变换矩阵
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[100,100],[200,50],[100,250]])
M = cv.getAffineTransform(pts1,pts2)
print(M)
dst = cv.warpAffine(img2,M,(cols,rows))
cv.imshow("before",img2)
cv.imshow("after",dst)
cv.waitKey(0)
cv.destroyAllWindows()