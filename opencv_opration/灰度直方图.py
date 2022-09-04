import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread("images/03-1.png",0)
hist = cv.calcHist([img],[0],None,[256],[0,256])
# cv.imshow("hise",hist)
# cv.waitKey(0)
# cv.destroyAllWindows()
plt.figure(figsize=(10,6),dpi= 100)
plt.plot(hist)
plt.grid()
plt.show()