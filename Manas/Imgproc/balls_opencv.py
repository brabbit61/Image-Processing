import cv2
import numpy as np

img1=cv2.imread('balls.jpeg')
img=cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
lower_green=np.array([50,100,100])
upper_green=np.array([70,255,255])
maskg = cv2.inRange(img, lower_green, upper_green)
lower_red=np.array([0,100,100])
upper_red=np.array([10,255,255])
maskr = cv2.inRange(img, lower_red, upper_red)
lower_blue=np.array([110,100,100])
upper_blue=np.array([130,255,255])
maskb = cv2.inRange(img, lower_blue, upper_blue)
resb = cv2.bitwise_and(img,img, mask= maskb)
resg = cv2.bitwise_and(img,img, mask= maskg)
resr = cv2.bitwise_and(img,img, mask= maskr)

res = cv2.add(maskg,maskr)
res=cv2.add(res,maskb)
final= cv2.bitwise_and(img1,img1,mask=res)
cv2.imshow('image',resb)
cv2.waitKey(0)
cv2.destroyAllWindows()
