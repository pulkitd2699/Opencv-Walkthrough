import cv2
import numpy as np

img = cv2.imread('m.jpeg',0)

#global histogram equilization
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
#cv2.imshow('res',res)

#adaptive histogram equilization
# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

cv2.imshow('clahe_2',cl1)

cv2.waitKey(0)
cv2.destroyAllWindows()