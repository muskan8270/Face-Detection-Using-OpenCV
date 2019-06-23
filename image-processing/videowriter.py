import numpy as np
import cv2
cap=cv2.VideoCapture("1.mp4")
fourcc=cv2.VideoWriter_fourcc(*'XVID')
fps=30
framesize=(720,480)
out=cv2.VideoWriter('sample.mp4',fourcc,fps,framesize)
while(cap.isOpened()):
    ret,frame=cap.read()
    cv2.imshow('frame',frame)
out.release()
cap.release()
