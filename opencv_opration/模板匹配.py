from unittest import result
import cv2 as cv
import numpy as np
img = cv.imread("images/lyy3.jpg")
template = cv.imread("images/lyy10.jpg")
h, w = template.shape[:2]
#模板匹配
res = cv.matchTemplate(img, template,cv.TM_CCORR)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0] + 5 , top_left[1] + 5)
#绘制矩形
cv.rectangle(img, top_left, bottom_right,(0,255,0),2)
cv.imshow("img",img)
cv.imshow("tem",template)
cv.waitKey(0)
cv.destroyAllWindows()