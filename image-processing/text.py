import numpy as np
import cv2
pic=np.zeros((500,500,3), dtype='uint8')
font=cv2.FONT_HERSHEY_DUPLEX
cv2.putText(pic, 'muuskan' ,(100,100), font, 3, (255,255,255), 4, cv2.LINE_8)
cv2.imshow('dark',pic)
cv2.waitkey(0)
