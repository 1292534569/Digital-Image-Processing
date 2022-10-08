import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread("./01.jpg")
#创建fast对象
fast = cv.FastFeatureDetector_create(threshold=30)
#检测
kp = fast.detect(img,None)
#绘制
img1 = cv.drawKeypoints(img,kp,None,color=(0,255,0))
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("./01.jpg")
#创建fast对象，注意fast可以处理彩色图像
fast = cv.FastFeatureDetector_create(threshold=30)
#检测关键点
kp = fast.detect(img,None)
#绘制关键点
img2 = cv.drawKeypoints(img, kp, None, color=(0,255,0))
#2022 09 19