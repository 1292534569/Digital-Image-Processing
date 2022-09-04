import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("./images/01.bmp")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#角点检测
corners = cv.goodFeaturesToTrack(gray, 20, 0.01, 10)
print(corners)
#绘制角点
for i in corners:
    i = i.astype(int)
    x,y = i.ravel()#将数组扁平化
    cv.circle(img,(x,y),20,(0,255,0),-1)
plt.figure(figsize=(20,10),dpi=100)
plt.imshow(img[:,:,::-1])
plt.show()