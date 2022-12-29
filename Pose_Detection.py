import cv2
from cvzone.PoseModule import  PoseDetector
import mediapipe as mp
import numpy as np


mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils
pose = mp_pose.Pose()


cap=cv2.VideoCapture("Video.mp4")
#cap=cv2.VideoCapture(0)

while True:
    ret , img = cap.read()
    img = cv2.resize(img,(600,400))

    results = pose.process(img)
    mp_draw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                           mp_draw.DrawingSpec((255, 0, 0), 2 , 2),
                           mp_draw.DrawingSpec((255 , 255 , 0) , 2 , 2)
                           )

    h, w, c = img.shape
    opimg = np.zeros([h, w, c])
    opimg.fill(255)
    mp_draw.draw_landmarks(opimg, results.pose_landmarks , mp_pose.POSE_CONNECTIONS,
                           mp_draw.DrawingSpec((255 , 0 , 255) , 2 , 2),
                           mp_draw.DrawingSpec((0 , 0 , 0) , 2 , 2))
    cv2.imshow("Pose Extact", opimg)


    print(results.pose_landmarks)
    cv2.imshow("Pose Estimation",img)
    key=cv2.waitKey(1)
    if key == ord('s'):
        with open("PoseFile.txt", 'w') as f:
            f.writelines(["%s\n" % item for item in opimg])
