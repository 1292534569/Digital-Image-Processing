import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
#创建一个空白图像
img = np.zeros((512,512,3),np.uint8)
#绘制图像
cv.line(img,(0,0),(511,511),(255,0,0),5)
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv.circle(img,(447,63),63,(0,0,255),-1)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,"opencv",(10,500),font,4,(255,255,255),2,cv.LINE_AA)
#显示
# cv.imshow("test02",img)
# cv.waitKey(0)
#cv.imread读进的是BGR，plt输出的是RGB，需要反转通道
plt.imshow(img[:,:,::-1])
plt.title("匹配结果"),plt.xticks([]),plt.yticks([])
plt.show()