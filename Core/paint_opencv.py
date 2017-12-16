import cv2
import numpy as np
drawing=False

def draw_circle(event,x,y,flags,param):
    global s,drawing,r,g,b
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing=True
    elif event== cv2.EVENT_MOUSEMOVE:    
        if drawing == True:
      	    cv2.circle(img,(x,y),s,(b,g,r),-1)
    elif event== cv2.EVENT_LBUTTONUP:
    	drawing=False
    	
def nothing(x):
    pass
img = np.zeros((512,512,3), np.uint8)
img[:]=255
cv2.namedWindow('image',cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback('image',draw_circle)
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('Size','image',0,20,nothing)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
    r=cv2.getTrackbarPos('R','image')
    g=cv2.getTrackbarPos('G','image')
    b=cv2.getTrackbarPos('B','image')
    s=cv2.getTrackbarPos('Size','image')      
cv2.destroyAllWindows()
