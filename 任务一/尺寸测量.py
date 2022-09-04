import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("./images/01.bmp")

#灰度化
gray_img = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
#二值化
ret,bin_img01 = cv.threshold(gray_img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
#反转颜色
bin_img = cv.bitwise_not(bin_img01)
#霍夫直线检测使极耳成为一个闭合轮廓
lines = cv.HoughLines(bin_img01,0.5,np.pi/180,150)
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 2000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv.line(bin_img,(x1,y1),(x2,y2),(0,255,0))
# #反转颜色
# bin_img = cv.bitwise_not(bin_img01)
#检测轮廓
# contours, hierarchy = cv.findContours(bin_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
plt.imshow(bin_img,cmap=plt.cm.gray)
# plt.imshow(gray_img[:,:,::-1])
plt.axis('off')
plt.show()
# cv.drawContours(img,contours,-1,(0,255,0),5)
#模板匹配
# template = cv.imread("images/tmp.jpg")
# h, w = template.shape[:2]
# res = cv.matchTemplate(img, template,cv.TM_CCORR)
# min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
# top_left = max_loc
# bottom_right = (top_left[0] + 5 , top_left[1] + 5)
# cv.rectangle(img, top_left, bottom_right,(0,255,0),2)
# plt.imshow(img[...,::-1])
# plt.axis('off')
# plt.show()

# cv.imwrite("images/tmp_img.bmp",bin_img)
# plt.imshow(img[...,::-1])
# plt.axis('off')
# plt.show()
