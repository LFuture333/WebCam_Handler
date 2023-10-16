import cv2
import numpy as np


def Get_Stream(webCam="enter the id number for the webcam"):
    opencv= cv2
    cap = opencv.VideoCapture(0)

    return opencv, cap

def Stream(cap,cv2):

    # capture  frame 
    ret, frame = cap.read()

    #Resize the frame
    #frame resizing option 
    size = (640, 480)

    #resize the frame to declare size
    frame = cv2.resize(frame, size)


    return frame
