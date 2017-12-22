import cv2
import numpy as np
def nothing(x):
	pass
vid=cv2.VideoCapture(0)
cv2.namedWindow('Pad',cv2.WINDOW_NORMAL)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
img = np.zeros((512,512,3), np.uint8)
cv2.createTrackbar('Size','Pad',0,20,nothing)
cv2.createTrackbar('Clear','Pad',0,1,nothing)
while vid.isOpened():
	_,frame=vid.read()
	frame=cv2.flip(frame,5)
	frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	greenLower = (29, 86, 6)
	greenUpper = (64, 255, 255)
	maskr = cv2.inRange(frame, greenLower,greenUpper)
	frame= cv2.Canny(maskr,100,200,L2gradient=True)
	frame=cv2.dilate(frame,None,iterations=2)
	frame=cv2.erode(frame,None,iterations=2)	
	frame=cv2.medianBlur(frame,1)
	_,contours,heirachy=cv2.findContours(frame,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	if contours is not None:
		for circle in contours:
			M=cv2.moments(circle)	
			if M['m00']==0:
				break
			perimeter = cv2.arcLength(circle,True)			
			x,y=int(M['m10']/M['m00']),int(M['m01']/M['m00'])
			s=cv2.getTrackbarPos('Size','Pad')
			check=cv2.getTrackbarPos('Clear','Pad')
			if check==1:
				img = np.zeros((512,512,3), np.uint8)
			if perimeter>130:
				cv2.circle(img,(x,y),s,(255,255,255),-1)
			
	cv2.imshow('image',frame)
	cv2.imshow('Pad',img)
	if  cv2.waitKey(1)==27:
		break	
vid.release()	
cv2.destroyAllWindows()
