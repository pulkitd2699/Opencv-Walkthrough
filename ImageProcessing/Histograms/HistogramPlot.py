#histogram - intensity distribution of an image
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('m.jpeg')
#hist = cv2.calcHist([img],[0],None,[256],[0,256])
#plt.hist(img.ravel(),256,[0,256]); plt.show()
#print(hist)

#color display
#color = ('b','g','r')
#for i,col in enumerate(color):
#    histr = cv2.calcHist([img],[i],None,[256],[0,256])
#    plt.plot(histr,color = col)
#    plt.xlim([0,256])
#plt.show()

#masking img
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:600, 100:600] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)

# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])

plt.show()