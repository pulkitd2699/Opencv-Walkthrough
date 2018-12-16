import numpy as np
import cv2
from common import Sketcher

img = cv2.imread('lc1.jpg')
mark = np.zeros(img.shape[:2], np.uint8)
sketch = Sketcher('img', [img, mark], lambda : ((255, 255, 255), 255))

dst = cv2.inpaint(img,mark,3,cv2.INPAINT_TELEA)

cv2.imshow('dst',dst)
cv2.imshow('mark',mark)
cv2.imshow('sketch',sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()