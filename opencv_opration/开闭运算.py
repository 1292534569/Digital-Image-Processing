import cv2 as cv
import numpy as np
img = cv.imread("images/07.png")
#创建内核
kernel = np.ones((10,10),np.uint8)
#开运算可以白点（亮斑）去除，闭运算可以将黑点（暗斑）去除
cv_open = cv.morphologyEx(img,cv.MORPH_OPEN,kernel)
cv_close = cv.morphologyEx(img,cv.MORPH_CLOSE,kernel)
#白色的为1
cv.imshow("before",img)
cv.imshow("open",cv_open)
cv.imshow("close",cv_close)
cv.waitKey(0)
cv.destroyAllWindows()
 