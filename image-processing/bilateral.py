import cv2
import numpy
pic=cv2.imread("1.jpg")
dipixel=7
color=100
space=100
filter =cv2.bilateralFilter(pic,dipixel,color,space)
cv2.imshow("filter",filter)
