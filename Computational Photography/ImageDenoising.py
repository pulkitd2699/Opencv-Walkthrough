import numpy as np
import cv2

img = cv2.imread('coins.jpg')

dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

cv2.imshow('img',img)
cv2.imshow('dst',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()