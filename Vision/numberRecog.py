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

    elif platform == 'Windows':
        return cv2.VideoCapture(cameraIndex, cv2.CAP_DSHOW)

def startCamera(): 
    cameraIndex = int(input('Which camera are you using (0 for main, 1 for secondary, and so on)?: '))
    cam = createCamera(cameraIndex)

    cv2.namedWindow('Video Feed Window')
    hwidth = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH)) // 2
    hheight = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT)) // 2
    # floor division because I don't want doubles

    while cam.isOpened():
        success, frame = cam.read()
        if not success: break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = frame[hheight - 50 : hheight + 50, hwidth - 125 : hwidth + 125] # weird that it is (y, x)
        frame = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 5)
        # https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
        cv2.imshow('Video Feed Window', frame)
        if cv2.waitKey(1) == 27: break

    cam.release()
    cv2.destroyAllWindows()

# testCameras()
startCamera()