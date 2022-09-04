import cv2 as cv
img1 = cv.imread("images/03.png")
rows,cols = img1.shape[:2]
print(rows,cols)
#绝对尺寸缩放
res = cv.resize(img1,(720,1080))
print(res.shape)
#相对尺寸缩放
res1 = cv.resize(img1,None,fx=0.4,fy=0.7)
print(res1.shape)
# cv.imshow("res1",res)
# cv.imshow("img",img1)
# cv.imshow("res2",res1)
cv.waitKey(0)
cv.destroyAllWindows()
 