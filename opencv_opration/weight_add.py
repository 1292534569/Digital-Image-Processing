import numpy as np
import cv2 as cv
img1 = cv.imread("images/rain.jpg")
img2 = cv.imread("images/view.jpg")
img3 = cv.addWeighted(img1,0.7,img2,0.3,0)
img4 = cv.addWeighted(img1,0.3,img2,0.7,10)
cv.imshow("image",img3)
cv.imshow("image01",img4)
cv.waitKey(0)
cv.destroyAllWindows()