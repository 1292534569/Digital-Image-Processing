import cv2 as cv
import numpy as np
img = cv.imread("images/07.png")
#均值滤波对附近每个像素的权重是一样的
blur = cv.blur(img,(10,10))
#高斯滤波对中心像素附近的像素值的权重不同
guss = cv.GaussianBlur(img,(7,3),1)
#中值滤波取像素附近的中值，不受最值影响，对椒盐噪声有效
mid = cv.medianBlur(img,5)
cv.imshow("before",img)
cv.imshow("blur",blur)
cv.imshow("guss",guss)
cv.imshow("mid",mid)
cv.waitKey(0)
cv.destroyAllWindows() 