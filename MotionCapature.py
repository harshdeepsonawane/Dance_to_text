import cv2
from cvzone.PoseModule import  PoseDetector
cap=cv2.VideoCapture("Video.mp4")
import mediapipe as mp

detector=PoseDetector()
posList= []
while True:
		success, img = cap.read();
		img = cv2.resize(img, (600, 400))
		img = detector.findPose(img)
		lmList, bboxInfo = detector.findPosition(img)

		if bboxInfo:
			lmString=''
			for lm in lmList:
				print(lm)
				lmString += f'[{lm[1]},{img.shape[0]-lm[2]},{lm[3],}]'
			posList.append(lmString)
		#print("Here")
		#print(posList)
		print(len(posList)) #number Of Frame Getting

		cv2.imshow("MotionCap",img)
		key=cv2.waitKey(1)
		if key == ord('s'):
			with open("MotionCap.txt",'w') as f:
				f.writelines(["%s\n"% item for item in posList])
