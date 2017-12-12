#!/usr/bin/env python 	
from __future__ import print_function
import numpy as np
import cv2
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge,CvBridgeError

def talker():
	frame_pub=rospy.Publisher('Lanes',Image , queue_size=1)
	bridge = CvBridge()
	rospy.init_node('talker', anonymous=True)
	rate=rospy.Rate(10)
	vid=cv2.VideoCapture("easier.mp4")
	while vid.isOpened():
		_,frame=vid.read()
		while not rospy.is_shutdown():
			#rospy.loginfo(frame)
			try:
				frame=bridge.cv2_to_imgmsg(frame, "bgr8")
			except CvBridgeError as e:
				print(e)
			frame_pub.publish(frame)
			rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

