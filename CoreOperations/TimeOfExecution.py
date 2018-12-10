import cv2
import time

img1 = cv2.imread('opencv_logo.jpg')

cc1 = cv2.getTickCount()
t1 = time.time()
for i in range(5,49,2):
    img1 = cv2.medianBlur(img1,i)
t2 = time.time()
cc2 = cv2.getTickCount()

cc_t = (cc2 - cc1)/cv2.getTickFrequency()
t_t = t2 - t1

print(cc_t)
print(t_t)
