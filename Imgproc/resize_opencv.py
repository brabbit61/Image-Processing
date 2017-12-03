import cv2
import numpy as np

img=cv2.imread('balls.jpeg')
rows,cols,_=img.shape
cv2.namedWindow('image',cv2.WINDOW_AUTOSIZE)
while rows>10:
	cv2.imshow('image',img)
	k=cv2.waitKey(100)
	if k==27:
		break
	img=cv2.resize(img,(cols-1,rows-1),interpolation=cv2.INTER_AREA)
	rows,cols,_=img.shape
	
cv2.destroyAllWindows()
