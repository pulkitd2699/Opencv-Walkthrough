import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow('frame')


cv2.createTrackbar('Min_Val','frame',0,255,nothing)
cv2.createTrackbar('Max_Val','frame',0,255,nothing)
    
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame,1)
    
    a = cv2.getTrackbarPos('Min_Val','frame')
    b = cv2.getTrackbarPos('Max_Val','frame')
    
    edges = cv2.Canny(frame,a,b)
    cv2.imshow('',edges)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break  
    
cv2.destroyAllWindows()
cap.release()