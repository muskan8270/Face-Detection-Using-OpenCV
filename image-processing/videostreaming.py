import cv2
import numpy
cap=cv2.VideoCapture("1.mp4")
while(cap.isOpened()):
    ret, frame= cap.read()
    cv2.imshow("vid",frame)
    if 0xFF ==ord('q'):
        break
    

    
