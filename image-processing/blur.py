import cv2
import numpy
pic=cv2.imread('1.jpg')
matrix=(7,7)
blur=cv2.GaussianBlur(pic,matrix,0)
cv2.imshow('blur',blur)
cv2.waitkey(0)
