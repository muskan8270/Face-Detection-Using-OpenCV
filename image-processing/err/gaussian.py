import cv2
import numpy
pic=cv2.imread("55.jpg")
kernal=3
median=cv2.medianBlur(pic ,kernal)

t=cv2.imshow("82",median)
cv2.imwrite("999.jpg",median)
