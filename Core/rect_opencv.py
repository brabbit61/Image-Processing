import cv2
import numpy as np
ix,iy=0,0
def draw_rect(event,x,y,flags,_):
    global ix,iy
    if event== cv2.EVENT_LBUTTONDOWN:
    	ix,iy=x,y
    elif event==cv2.EVENT_LBUTTONUP:
        cv2.rectangle(img,(ix,iy),(x,y),(255,255,255),1)
        
img=np.zeros((500,500,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_rect)
while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)
    if k==27:
        break
 

