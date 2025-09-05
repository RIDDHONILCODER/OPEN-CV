import cv2
image=cv2.imread('pic.jpg')
cv2.namedWindow('Car image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Car image',600,400)
cv2.imshow('Car image',image)
cv2.waitKey(0)
cv2.destroyWindow()