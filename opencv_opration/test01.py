import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# 读取图像
img = cv.imread("./images/03.png",0)
#2 显示图像
#用cv显示图像
cv.imshow("image",img)
cv.waitKey(0)
cv.destroyAllWindows()
#在matplotlib中显示
plt.imshow(img,cmap=plt.cm.gray)
plt.title("匹配结果"),plt.xticks([]),plt.yticks([])
plt.show()
k=cv.waitKey()
# cv.imwrite("images/messigray.png",img)