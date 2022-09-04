import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt 
# img = np.zeros((256,256,3),np.uint8)

# img[100,100] = (0,0,255)
# px = img[100,100]
# # print(px)
# # cv.imshow("image",img)
# # cv.waitKey(0)
# print(img.shape)
# print(img.dtype)
# print(img.size)
img = cv.imread("C/Users/12925/Desktop/cv/images/02.jpg")
b,g,r = cv.split(img)
img2 = cv.merge((b,g,r))
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("img1",img)
cv.imshow("img",hsv)
cv.waitKey(0)