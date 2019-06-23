import cv2
import numpy as np
pic=cv2.imread('1.jpg')
rows=pic.shape[0]
cols=pic.shape[0]
center=(cols/2,rows/2)
angle=-90
m=cv2.getRotationMatrix2D(center,angle,1)
rotate=cv2.warpAffine(pic,m,(cols,rows))
cv2.imshow('dark',rotate)

