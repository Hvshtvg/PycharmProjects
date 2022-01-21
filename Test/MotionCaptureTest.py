import cv2
import mediapipe as mp
import time

cam = cv2.VideoCapture(1)

while True:
    success, img = cam.read()
    cv2.imshow("Webcam image", img)
    cv2. waitKey(1)