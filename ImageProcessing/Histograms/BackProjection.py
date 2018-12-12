import cv2
import numpy as np
from matplotlib import pyplot as plt

roi = cv2.imread('AW 1.jpg')
hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

target = cv2.imread('AW.jpg')
hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)

# calculating object histogram
roihist = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )

# normalize histogram and apply backprojection
cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
mask = cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)

# Now convolute with circular disc
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
mask = cv2.filter2D(mask,-1,kernel,mask)

# threshold and binary AND
ret,thresh = cv2.threshold(mask,50,255,0)
thresh = cv2.merge((thresh,thresh,thresh))
res = cv2.bitwise_and(target,thresh)

res = np.vstack((target,thresh,res))

#plt.imshow(roihist)
#plt.show()
#cv2.imshow('thresh',thresh)
cv2.imshow('res',res)

cv2.waitKey(0)
cv2.destroyAllWindows()
