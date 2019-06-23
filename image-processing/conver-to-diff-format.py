import numpy as np
import cv2
img = cv2.imread('1.jpg')
img= cv2.imwrite('2.png',img)
cv2.imshow('hey',img)
cv2.waitKey(0)

