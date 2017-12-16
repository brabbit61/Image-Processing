import cv2
import numpy as np

def nothing(x):
	pass
cv2.namedWindow('Convertor',cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('B','Convertor',0,255,nothing)
cv2.createTrackbar('G','Convertor',0,255,nothing)
cv2.createTrackbar('R','Convertor',0,255,nothing)
img=np.zeros((500,500,3),np.uint8)
cv2.imshow('Convertor',img)
previous=[0,0,0]	
while cv2.waitKey(1)!=27:
	b=cv2.getTrackbarPos('B','Convertor')
	g=cv2.getTrackbarPos('G','Convertor')
	r=cv2.getTrackbarPos('R','Convertor')
	img[:]=(b,g,r)
	cv2.imshow('Convertor',img)
	if [b,g,r]!=previous:
		previous=[b,g,r]
		x=np.uint8([[[b,g,r]]])
		x=cv2.cvtColor(x,cv2.COLOR_BGR2HSV)
		print x
cv2.destroyAllWindows()
