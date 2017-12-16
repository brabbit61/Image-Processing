import cv2
import numpy as np

img=cv2.imread('balls.jpeg')
img=cv2.resize(img,(200,200))
r,c,_=img.shape
i=0
while r>10:
	cv2.imshow('image',img)
	k=cv2.waitKey(300)
	if k==27:
		break
	i+=1
	img=img[i:r-i,i:c-i]
	img=cv2.resize(img,(200,200),cv2.INTER_CUBIC)
