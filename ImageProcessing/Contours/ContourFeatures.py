import cv2
import numpy as np

img = cv2.imread('lc.jpg',0)
ret,thresh = cv2.threshold(img,127,255,0)
_,contours,hierarchy = cv2.findContours(thresh, 1, 2)

#finding contours
cnt = contours[0]
M = cv2.moments(cnt)
#print(M)

#centroids
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

#area od contour
area = cv2.contourArea(cnt)

#perimeter of contour
perimeter = cv2.arcLength(cnt,True)

#contour approximation
epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)

#convex hull
hull = cv2.convexHull(cnt)

#checking the convexity
k = cv2.isContourConvex(cnt)

#bounding rectangle-straight
x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

#bounding rectangle-rotated
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img,[box],0,(0,0,255),2)

#min enclosing circle
(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
cv2.circle(img,center,radius,(0,255,0),2)

#fitting an ellipse
ellipse = cv2.fitEllipse(cnt)
cv2.ellipse(img,ellipse,(0,255,0),2)

#fitting a line
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)