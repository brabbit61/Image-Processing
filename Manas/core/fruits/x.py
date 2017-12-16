import cv2
import numpy as np

img=cv2.imread('1.jpeg')		
img=cv2.pyrDown(img)			#that level
lower=cv2.pyrDown(img)			#lvel above
higher=cv2.pyrUp(lower)			#expanded	
cv2.imshow('image',cv2.subtract(img,higher))
cv2.waitKey(0)
cv2.destroyAllWindows()
