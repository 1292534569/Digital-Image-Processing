#coding = utf-8
from ctypes import sizeof
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
#灰度二值化
ret,thresh1 = cv.threshold(gray,200,255,cv.THRESH_BINARY)#定位用
ret1,bina = cv.threshold(gray,150,255,cv.THRESH_BINARY)#测量用

img_morph = thresh1.copy()                             # 复制图像
cv.erode(img_morph, (100,100), img_morph, iterations= 10)   # 腐蚀运算
cv.dilate(img_morph, (50,50), img_morph, iterations= 10)  # 膨胀运算

#获取图像特征
cnts, _ = cv.findContours(img_morph, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) # 获取图像轮廓
cnts_sort = sorted(cnts, key= cv.contourArea, reverse= True) # 将轮廓包含面积从大到小排列
box = cv.minAreaRect(cnts_sort[0]) # 选取包含最大的两个面积的轮廓，并得出最小外接矩形
box1 = cv.minAreaRect(cnts_sort[1]) # 选取包含最大的两个面积的轮廓，并得出最小外接矩形
points = np.int0(cv.boxPoints(box))# 获得该矩形的四个定点
points1 = np.int0(cv.boxPoints(box1))# 获得该矩形的四个定点
cen_v = (points[0,0] + points[2,0]) / 2                 # 得出横向中心
cen_v1 = (points1[0,0] + points1[2,0]) / 2                 # 得出横向中心
cen_h = (points[0,1] + points[2,1]) / 2                 # 得出纵向中心
cen_h1 = (points1[0,1] + points1[2,1]) / 2                 # 得出纵向中心

#在原图上绘制
cv.drawContours(img, [points], -1, (0,255,0), 20) 
cv.drawContours(img, [points1], -1, (0,255,0), 20) 

# 尺寸测量
cnts1, hrchy= cv.findContours(bina.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
cnts1 = imutils.grab_contours(cnts1)
# 对轮廓点进行排序
(cnts1, _) = contours.sort_contours(cnts1)

ls = [] 
# print(cnts1[128])
# 循环遍历每一个轮廓点
# for i in range(200):
#     print(cnts1[i])
#从右向左，d0-dn
wr = cnts1[1280]-cnts1[274]#右极耳的宽度为wr
wr1 = wr[0,0]
rat = cnts1[861]-cnts1[520]#右AT11宽度
rat1 = rat[0,0]

#puttext
cv.putText(img,"rigth tab width-"+str(wr1),(50,250),cv.FONT_HERSHEY_COMPLEX,4,(0,0,255),3)
cv.putText(img,"rigth AT11 width-"+str(rat1),(50,150),cv.FONT_HERSHEY_COMPLEX,4,(0,0,255),3)

plt.figure(figsize=(15,7),dpi=100)
plt.xticks([]),plt.yticks([])
plt.imshow(img[:,:,::-1])
# plt.imshow(bina,cmap='gray')
plt.show()