import cv2
import numpy as np

img = cv2.imread('lc.jpg',0)
ret,thresh = cv2.threshold(img,127,255,0)
_,contours,hierarchy = cv2.findContours(thresh, 1, 2)

#finding contours
cnt = contours[0]
M = cv2.moments(cnt)
#print(M)

#Aspect ratio
x,y,w,h = cv2.boundingRect(cnt)
aspect_ratio = float(w)/h

#extent
area = cv2.contourArea(cnt)
x,y,w,h = cv2.boundingRect(cnt)
rect_area = w*h
extent = float(area)/rect_area

#solidity
area = cv2.contourArea(cnt)
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area)/hull_area

#equivalent diameter
area = cv2.contourArea(cnt)
equi_diameter = np.sqrt(4*area/np.pi)

#Orientation
(x,y),(MA,ma),angle = cv2.fitEllipse(cnt)

#mask and pixel points
mask = np.zeros(imgray.shape,np.uint8)
cv2.drawContours(mask,[cnt],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask))
#pixelpoints = cv2.findNonZero(mask)

#maximum value, min value and their locations
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(imgray,mask = mask)

#mean color and mean intensity
mean_val = cv2.mean(im,mask = mask
                    
#extreme points
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])                    