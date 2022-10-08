from sys import flags
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("./images/01.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#SIFT关键点检测
#实例化SIFT
#opencv 4.3以后用SIFT_create
sift = cv.SIFT_create()
#3.4以前用下面的语句初始化
# sift = cv.xfeatures2d.SIFT_create()
#def为关键点的描述
kp,des = sift.detectAndCompute(gray,None)
print(des)
#最后一个参数为绘制方式
cv.drawKeypoints(img,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
plt.figure(figsize=(10,13),dpi=100)
plt.imshow(img[:,:,::-1])
plt.xticks([]),plt.yticks([])
plt.show()