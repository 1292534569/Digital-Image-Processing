#coding = utf-8
from imutils import perspective
from imutils import contours
from scipy.spatial import distance as dist
import numpy as np
import argparse
import cv2 as cv
import imutils
import matplotlib.pyplot as plt
#读入图片
img = cv.imread("./images/02.bmp")
#灰度化
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#高斯滤波
gray = cv.GaussianBlur(gray,(7,7),0)

#边缘检测获取AT11
edged = cv.Canny(gray,50,100)
#膨胀与腐蚀
edged = cv.dilate(edged,None, iterations=1)
edged = cv.erode(edged,None, iterations=1)

#在边缘图像中寻找轮廓
cnts, hrchy= cv.findContours(edged.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img,cnts,-1,(0,0,255),1)
# cnts = imutils.grab_contours(cnts)
# print(cnts.shape())

#遍历轮廓
# i = cnts[0:10]
# print(i)
for c in cnts:
    #如果当前轮廓面积过小，认为是噪声
    if cv.contourArea(c) > 100:
        continue

    # print("c",c)
    # print("---")
    # print("c+1",cnts[c+1])

    # for i = c+1 in cnts:
        
    print(c)
    #获取每条直线之间的距离


plt.figure(figsize=(15,7),dpi=100)
plt.imshow(img[:,:,::-1])
plt.show()