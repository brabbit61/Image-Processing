import cv2
import numpy as np

cv2.namedWindow('image',cv2.WINDOW_AUTOSIZE)
for i in range(1,3):
	img1=cv2.imread('/home/jenit1/Desktop/core/fruits/'+str(i)+'.jpeg')
	img2=cv2.imread('/home/jenit1/Desktop/core/fruits/'+str(i+1)+'.jpeg')
	img1=cv2.resize(img1,(100,100))
	img2=cv2.resize(img2,(100,100))
	x,y=0,1
	for j in range(20):
		img=cv2.addWeighted(img2,x,img1,y,0)
		cv2.imshow('image',img)
		cv2.waitKey(100)
		x+=0.05
		y-=0.05
cv2.destroyAllWindows()

