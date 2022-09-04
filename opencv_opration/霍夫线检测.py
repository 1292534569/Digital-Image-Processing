import cv2 as cv
import numpy as np
img = cv.imread("./images/11.png")
#二值化
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray,50,150)
#霍夫直线变换
lines = cv.HoughLines(edges,0.5,np.pi/180,150)
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
    cv.line(img,(x1,y1),(x2,y2),(0,255,0))
cv.imshow("img",img)
cv.waitKey(0)
cv.destroyAllWindows()
