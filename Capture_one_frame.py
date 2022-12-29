import cv2
from cvzone.PoseModule import  PoseDetector
cap=cv2.VideoCapture("Video.mp4")
import numpy as np
import mediapipe as mp

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils
pose = mp_pose.Pose()
detector = PoseDetector()
posList= []
count=0
while True:
		if count == 25: break
		success, img = cap.read();
		img = cv2.resize(img, (600, 400))
		img = detector.findPose(img)
		lmList, bboxInfo = detector.findPosition(img)

		results = pose.process(img)

		if bboxInfo:
			lmString=''
			for lm in lmList:
				print(lm)
				lmString +=f'[{lm[1]},{img.shape[0]-lm[2]},{lm[3],}]'
			posList.append(lmString)
		print("Here is List Of Cordinate Of Frames-:")
		print(posList)

		print(len(posList)) #number Of Frame Getting
		h, w, c = img.shape
		opimg = np.zeros([h, w, c])
		opimg.fill(255)
		mp_draw.draw_landmarks(opimg, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
							  	 mp_draw.DrawingSpec((255, 0, 255), 2, 2),
							   	mp_draw.DrawingSpec((0, 0, 0), 2, 2))
		cv2.imshow("Pose Extact", opimg)


		cv2.imshow("Image",img)
		key=cv2.waitKey(1000000)
		if key == ord('s'):
			with open("Cordinate_one_frame.txt",'w') as f:
				f.writelines(["%s\n"%  item for item in posList])
		count+=1