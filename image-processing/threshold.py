import cv2
import numpy
#p=cv2.imread('crack1.jpg')
pic=cv2.imread('55.jpg',0)
th=100
(T_value,a)=cv2.threshold(pic,th,255,cv2.THRESH_BINARY_INV)
#cv2.imshow('binary',a)
#pic=cv2.imwrite('m2.jpg',pic)
cv2.imshow('binary',a)
print(pic)
#cv2.imshow('original',p)
