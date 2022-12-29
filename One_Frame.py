import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture("Video.mp4")

detector = PoseDetector()
posList = []
count = 0
while True:
    if count == 1: break
    success, img = cap.read()
    img = cv2.resize(img, (500, 500))
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img)

    if bboxInfo:
        lmString = ''
        for lm in lmList:
            print(lm)
            lmString += f'{lm[1]},{img.shape[0] - lm[2]},{lm[3],}'
        posList.append(lmString)

    # print("Here")
    # print(posList[0])# print matrix of image
    # print(len(posList)) #number Of Frame Getting

    cv2.imshow("Image", img)
    key = cv2.waitKey(10000)
    if key == ord('k'):
        with open("Filenew.txt", 'w') as f:
            f.writelines(["%s\n" % posList[0]])

    count += 1