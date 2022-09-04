import cv2 as cv
import numpy as np
img = cv.imread("./images/12.jpg")
#sobel算子计算卷积结果
x = cv.Sobel(img, cv.CV_16S,1,0)
y = cv.Sobel(img, cv.CV_16S,0,1)
#scharr算子，ksize为-1,用于检测细小边缘
x1 = cv.Sobel(img, cv.CV_16S,1,0, ksize=-1)
y1 = cv.Sobel(img, cv.CV_16S,0,1, ksize=-1)
#laplacian转换
lap = cv.Laplacian(img,cv.CV_16S)
scale_abs = cv.convertScaleAbs(lap)#16位的无法显示，需要转换成uint8位的
#canny
low_thre = 0
high_thre = 100
canny = cv.Canny(img,low_thre,high_thre)

#转换数据
abs_x = cv.convertScaleAbs(x)
abs_y = cv.convertScaleAbs(y)
abs_x1 = cv.convertScaleAbs(x1)
abs_y1 = cv.convertScaleAbs(y1)
#结果合成
res = cv.addWeighted(abs_x,0.5, abs_y, 0.5, 0)
res1 = cv.addWeighted(abs_x1,0.5, abs_y1, 0.5, 0)
cv.imshow("before",img)
cv.imshow("res",res)
cv.imshow("res1",res1)
cv.imshow("lap",scale_abs)
cv.imshow("canny",canny)
cv.waitKey(0)
cv.destroyAllWindows()