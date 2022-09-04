import cv2 as cv
import numpy as np
img = cv.imread("images/07.png")
#创建内核
kernel = np.ones((10,10),np.uint8)
#礼帽用来分离背景亮斑，黑帽用来分离出暗斑
cv_tophat = cv.morphologyEx(img,cv.MORPH_TOPHAT,kernel)
cv_black = cv.morphologyEx(img,cv.MORPH_BLACKHAT,kernel)

cv.imshow("before",img)
cv.imshow("tophat",cv_tophat)
cv.imshow("black",cv_black)
cv.waitKey(0)
cv.destroyAllWindows()
 