import cv2
import numpy as np
pic=cv2.imread('1.jpg')
cols= pic.shape[1]
rows= pic.shape[0]
m=np.float32([[1,50,50],[0,1,70]])
shifted=cv2.warpAffine(pic, m, (cols, rows))
cv2.imshow('shifted',shifted)
cv2.waitkey(0)
