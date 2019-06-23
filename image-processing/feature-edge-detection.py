import cv2
import numpy
pic=cv2.imread("55.jpg")
thresholdval1=150
thresholdval2=100
canny=cv2.Canny(pic,thresholdval1,thresholdval2)
cv2.imshow("canny",canny)
