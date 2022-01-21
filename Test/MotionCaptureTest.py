import cv2
import mediapipe as mp
import time

# Volba web kamery - 0 = integrovaná, 1 = externí
cam = cv2.VideoCapture(1)

mpHands = mp.solutions.hands
hands = mpHands.Hands() #ctrl+klik k více informacím o parametrech
mpDraw = mp.solutions.drawing_utils
pTime = 0 #previous time
cTime = 0 #current time

while True:
    success, img = cam.read()  #turn on camera
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(cx, cy)
                if id == 0:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    #FPS counter top left
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.imshow("Webcam image", img) # camera window
    cv2.waitKey(1)
