import cv2 as cv
import numpy as np
img = cv.imread("images/03.png")
res = cv.resize(img,None,fx=0.5,fy=0.5)
rows,cols = res.shape[:2]
M = np.float32([[1,0,100],[0,1,40]])
dst = cv.warpAffine(res,M,(2*cols,2*rows))
cv.imshow("res",res)
cv.imshow("dst", dst)
cv.waitKey(0)
cv.destroyAllWindows()