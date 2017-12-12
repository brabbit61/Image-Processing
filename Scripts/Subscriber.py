#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import rospy
from sensor_msgs.msg import Image
import cv2
import numpy as np

def callback(data):
	bridge=CvBridge()
	try:
		img=bridge.imgmsg_to_cv2(data,"bgr8")
	except CvBridgeError as e:
				print(e)
	w,h,_=img.shape											#dimensions of the img
	finaly=np.zeros((w,h,3),np.uint8)						#black background for yellow color detection
	finalw=np.zeros((w,h,3),np.uint8)						#black background for white color detection
	yellow_lower=(20,130,150)								#threshold values
	yellow_upper=(30,240,255)
	white_lower=(206,195,181)
	white_upper=(255,255,255)
	framey=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)				#detection of yellow color
	masky = cv2.inRange(framey, yellow_lower,yellow_upper)	#mask for yellow color
	maskw = cv2.inRange(img, white_lower,white_upper)		#mask for white color
	finaly=cv2.cvtColor(finaly,cv2.COLOR_BGR2GRAY)			#grayscale for the detected yellow color
	finalw=cv2.cvtColor(finalw,cv2.COLOR_BGR2GRAY)			#grayscale for the detected white color
	finaly[400:650,250:1200]=masky[400:650,250:1200]		#cropping the part of the road only
	finalw[400:650,250:1200]=maskw[400:650,250:1200]		#cropping the part of the road only
	finaly=cv2.GaussianBlur(finaly,(3,3),0)
	finalw=cv2.GaussianBlur(finalw,(3,3),0)
	#for the yellow lines on the road
	frame= cv2.Canny(finaly,50,150,L2gradient=True)			#Find the outlines of the yellow lines on the road
	frame=cv2.dilate(frame,None,iterations=3)
	frame=cv2.erode(frame,None,iterations=1)
	_,contours,heirachy=cv2.findContours(finaly,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)	#finding contours in the image
	if contours is not None:
		for cnt in contours:
			#rect = cv2.minAreaRect(cnt)					#finding the minimum bounding rectangle
			x,y,w,h = cv2.boundingRect(cnt)			
			M=cv2.moments(cnt)
			if M['m00']<100:
				continue
			cv2.line(img,(x,y+h),(x+w,y),(0,0,255),9)
			m=-h/float(w)									#slope of the yellow line		
			c=y+h-m*(x)										#intercept of the yellow line
			#if (cv2.contourArea(cnt)/(rect[1][0]*rect[1][1]))>0.5:	#finding the extent of the contour to check whether its a line or not
			#	cv2.drawContours(img,[cnt],0,(0,0,255),-1)
				
			break
	#for white lines
	frame= cv2.Canny(finalw,50,150,L2gradient=True)			#Find the outlines of the white lines on the road
	frame=cv2.dilate(frame,None,iterations=3)
	frame=cv2.erode(frame,None,iterations=1)
	lines = cv2.HoughLinesP(frame, 1, np.pi/180,175,minLineLength=60,maxLineGap=200)														
	m=0
	if lines is not None:
		slopepos=[]
		intercepts=[]
		for x in lines:
			for y in x:
				m=(y[3]-y[1])/float(y[2]-y[0])
				if m>0.45:
					c=y[1]-m*y[0]
					intercepts.append(c)
					slopepos.append(m)
					dist=abs(cordpos[0]-y[0])+abs(cordpos[1]-y[1])
					if dist<30:
						continue
					cordpos=[y[0],y[1]]
		
		if len(slopepos)>0:
			c=sum(intercepts)/len(intercepts)				# y intercept
			m=sum(slopepos)/len(slopepos)					#Slope for the white lines		
			m=np.arctan(m)
			if m>0.45:											#to exclude lines that have very low degree of inclination eg 1,2 degrees			
				x2= int(cordpos[0]+285*np.cos(m))
				y2= int(cordpos[1]+285*np.sin(m))
				cv2.line(img,(cordpos[0],cordpos[1]),(x2,y2),(0,0,255),9)
				#cv2.line(img,(cordpos[0],cordpos[1]),(0,int(c)),(0,0,255),9)	
	else:
		#if framenum!=1:
		cv2.line(img,(cordpos[0],cordpos[1]),(x2,y2),(0,0,255),9)
		#cv2.line(img,(cordpos[0],cordpos[1]),(0,int(c)),(0,0,255),9)

	cv2.imshow('frame',img)
	
	cv2.waitKey(1)
	cv2.destroyAllWindows()

def listener():
	rospy.init_node('listener', anonymous=True)
  	rospy.Subscriber('chatter', Image , callback)
  	rospy.spin()

if __name__ == '__main__':
	listener()
