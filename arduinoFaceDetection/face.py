# code mostly from: https://www.learnrobotics.org/blog/face-tracking-opencv/

import numpy as np
import serial
import time
import cv2

# Setup Communication path for arduino
arduino = serial.Serial(port='/dev/cu.usbmodem14201', baudrate=9600)
time.sleep(2)
print("Connected to Arduino...")

# importing the Haarcascadeq
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture the video stream from webcam.
cap = cv2.VideoCapture(1)

if (cap.isOpened() == False):
    print("Error opening video stream or file")

while (cap.isOpened()):
    ret, frame = cap.read()  # ret is a bool, checks if the frame is returning anything??

    if (ret):
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        # Detect faces in the image:
        faces = faceCascade.detectMultiScale( # detectMultiScale is a "general function that detects objects"
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        # ^this returns a list full of rectangles where faces are

        # print("Found this many faces: ", len(faces))

        for (x, y, w, h) in faces:
            # Display/draw a rectangle around the faces
            #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # find the center of the rect:
            xMid = int(x + (x + h) / 2)
            print('xMid: ', xMid)

            arduino.write(str(xMid).encode())

            #print('arduino: ', arduino.readline())

        #cv2.imshow("Faces found", frame)

        # Hit 'q' to terminate execution
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        print("It didn't work...")
        break

