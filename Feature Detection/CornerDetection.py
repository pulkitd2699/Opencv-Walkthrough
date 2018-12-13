import cv2
import numpy as np

img = cv2.imread('lc.jpg')
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5) 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)
    
cv2.imshow('',img)