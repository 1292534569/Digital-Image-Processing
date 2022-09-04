import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("./images/02.png")
# img = cv.imread("./images/01.bmp")
# guss = cv.GaussianBlur(img,(7,3),1)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# ret,bin_img01 = cv.threshold(gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
#反转颜色
# bin_img = cv.bitwise_not(bin_img01)
#角点检测
# bin_img = np.float32(bin_img)
dst = cv.cornerHarris(gray,2,3,0.04)
img[dst>0.001*dst.max()] = [255,255,255]
plt.figure(figsize=(10,8),dpi=100)
plt.imshow(img[:,:,::-1]),plt.title("角点检测")
plt.xticks([]),plt.yticks([])
plt.show()
