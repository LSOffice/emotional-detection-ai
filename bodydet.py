import cv2
from cvzone.PoseModule import PoseDetector

detector = PoseDetector()
cap = cv2.VideoCapture(0)
count = 0
while True:
    response, img = cap.read()
    if response == False:
        print("untrue")

    img = detector.findPose(img)
    lmlist, bbox = detector.findPosition(img)
    cv2.imshow("ImageWindow", img)
    #cv2.imwrite("./imshow/frame%d.jpg" % count, img)
    print(count)
    cv2.waitKey(1)
    count += 1