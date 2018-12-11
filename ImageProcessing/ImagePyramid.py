import cv2

img = cv2.imread("opencv_logo.png")

layer = img.copy()

#Gaussian Pyramid
gaussian_pyramid = [layer]
for i in range(4):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid.append(layer)
    
#Laplacian Pyramid
layer = gaussian_pyramid[3]
laplacian_pyramid = [layer]
for i in range(3, 0, -1):
    size = (gaussian_pyramid[i-1].shape[1], gaussian_pyramid[i-1].shape[0])
    gaussian_expanded = cv2.pyrUp(gaussian_pyramid[i], dstsize=size)
    laplacian = cv2.subtract(gaussian_pyramid[i-1], gaussian_expanded)
    laplacian_pyramid.append(laplacian)
    cv2.imshow(str(i), laplacian)
    
cv2.waitKey(0)
cv2.destroyAllWindows