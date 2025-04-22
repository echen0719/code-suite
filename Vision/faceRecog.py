import os
os.environ['OPENCV_LOG_LEVEL'] = 'SILENT'
import cv2
import platform

platform = platform.system()

def testCameras():
    working = 'Ports Working: '
    for port in range(0, 17):
        cam = createCamera(port)
        check, frame = cam.read()
        if check: working += str(port) + ' '
    print(working)

def createCamera(cameraIndex):
    if platform == 'Linux':
        return cv2.VideoCapture(cameraIndex)
        print('Cannot open webcam')
        exit

    elif platform == 'Windows':
        return cv2.VideoCapture(cameraIndex, cv2.CAP_DSHOW)
        print('Cannot open webcam')
        exit

def detectFaces():
    cameraIndex = int(input('Which camera are you using (0 for main, 1 for secondary, and so on)?: '))
    cam = createCamera(cameraIndex)

    cv2.namedWindow('Video Feed Window')
    classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    
    while cam.isOpened():
        success, frame = cam.read()
        if not success: break
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = classifier.detectMultiScale(grayFrame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for rect in face:
            cv2.rectangle(frame, rect, (0, 255, 0), 3)

        cv2.imshow('Video Feed Window', frame)
        if cv2.waitKey(1) == 27: break # press 'ESC' to exit

    cam.release()
    cv2.destroyAllWindows()

testCameras()
detectFaces()