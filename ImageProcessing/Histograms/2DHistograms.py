import cv2
from matplotlib import pyplot as plt


img = cv2.imread('m.jpeg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

#Note While using this function, remember, interpolation flag should be nearest for better results.

plt.imshow(hist,interpolation = 'nearest')
plt.show()