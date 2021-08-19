import cv2
import mediapipe as mp #pip install mediapipe
import time
pTime = 0

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
if file_path==():
    exit()

cap = cv2.VideoCapture(file_path)

while True:
    if file_path.find(".png")>0 or file_path.find(".jpg")>0:
        img = cv2.imread(file_path)
    else:
        success, img = cap.read()
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

    cv2.imwrite("test.jpg", img)
    cv2.imshow("Image", img)

    key = cv2.waitKey(1)
    if key == 27: #ESC
        break
