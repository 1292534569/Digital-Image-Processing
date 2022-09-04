import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread("images/12.jpg",0)
hist = cv.calcHist([img],[0],None,[256],[0,256])
dst = cv.equalizeHist(img)
dst_hist = cv.calcHist([dst],[0],None,[256],[0,256])
#创建自适应均衡化的对象 第一个参数为对比度的阈值，第二个参数为将图分成多少个小块
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
cv.imshow("img",img)
cv.imshow("dst",dst)
cv.imshow("cl1",cl1)
cv.waitKey(0)
cv.destroyAllWindows()
#直方图的显示
# plt.figure(figsize=(10,6),dpi= 100)
# plt.plot(hist)
# plt.plot(dst_hist)
# plt.grid()
# plt.show()