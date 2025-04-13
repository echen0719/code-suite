import os
os.environ['OPENCV_LOG_LEVEL'] = 'SILENT'
# stop warnings that fill console
import cv2
import platform

# https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html

platform = platform.system()

def testCameras():
    working = 'Ports Working: '
    for port in range(0, 17): # up to 16 devices
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

def takeImage(sizeX, sizeY, fileName):
    cameraIndex = int(input('Which camera are you using (0 for main, 1 for secondary, and so on)?: '))
    cam = createCamera(cameraIndex)

    cam.set(cv2.CAP_PROP_FRAME_WIDTH, sizeX)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, sizeY)

    while cam.isOpened():
        success, frame = cam.read()
        if not success: break
        cv2.imshow('Picture Feed Window', frame)

        keyPress = cv2.waitKey(1)
        if keyPress != -1 and keyPress != 27:
            cv2.imwrite(fileName, frame)
            break
        elif keyPress == 27 and fileName:
            break # empty string to not save

    cam.release()
    cv2.destroyAllWindows()

testCameras()
takeImage(640, 480, 'out.jpg')
