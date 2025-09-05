import cv2
image=cv2.imread('pic.jpg')
#converting to gray scale image#cv2.cvt color
image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
resizeimage=cv2.resize(image_gray,(220,220))
cv2.namedWindow('Car image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Car image',600,400)
cv2.imshow('Car image',image)
cv2.imshow('Gray scale Car image',resizeimage)
key=cv2.waitKey(0)
if key==ord('s'):
    cv2.imwrite('grayscaleresizedimage',resizeimage)

cv2.destroyWindow()
