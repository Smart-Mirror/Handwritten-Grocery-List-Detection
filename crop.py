import cv2
import numpy as np
im = cv2.imread("1.png")  
#im = cv2.resize(im,(600, 500), interpolation = cv2.INTER_CUBIC)
# Convert to grayscale and apply Gaussian filtering
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
im = cv2.GaussianBlur(im, (5, 5), 0)
# Threshold the image
#im_th = cv2.adaptiveThreshold(im_gray,255,1,1,11,2)
ret, im_th = cv2.threshold(im, 90, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("cropped", im_th)
cv2.imwrite("1.png",im_th)
cv2.waitKey(0),
