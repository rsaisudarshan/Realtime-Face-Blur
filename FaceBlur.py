import cv2 as cv
from cvzone.FaceDetectionModule import FaceDetector
cap = cv.VideoCapture(0)
detector = FaceDetector(minDetectionCon=0.75)
while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img,draw=True)
    if bboxs:
        for i,bbox in enumerate(bboxs):
            x,y,w,h = bbox['bbox']
            if x < 0: x=0
            if y<0: y=0
            imgCrop = img[y:y+h,x:x+w]
            imgBlur = cv.blur(imgCrop,(35,35))
            img[y:y+h,x:x+w]=imgBlur
    cv.imshow('Face Blur', img)
    cv.waitKey(1)