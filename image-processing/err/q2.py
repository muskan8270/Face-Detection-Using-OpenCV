import numpy as np
import cv2
pic =np.zeros((500,500,3),dtype='uint8')
cv2.rectangle(pic,(10,10),(50,15),(500,200,300),3,lineType=8,shift=0)
cv2.imshow('dark',pic)
cv2.waitKey(0)
