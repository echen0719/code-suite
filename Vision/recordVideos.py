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

def recordVideo(fileName, vidFormat, fps, sizeX, sizeY):
    cameraIndex = int(input('Which camera are you using (0 for main, 1 for secondary, and so on)?: '))
    cam = createCamera(cameraIndex)

    # cv2.VideoCapture() doesn't work if output and input dimensions aren't equal
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, sizeX)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, sizeY)
    cam.set(cv2.CAP_PROP_FPS, fps)

    print('Started!') # start confirm
    out = cv2.VideoWriter(fileName, cv2.VideoWriter_fourcc(*vidFormat), fps, (sizeX, sizeY))
    
    while cam.isOpened():
        success, frame = cam.read()
        if not success: break
        out.write(frame) # write before view
        cv2.imshow('Video Feed Window', frame)
        if cv2.waitKey(1) == 27: break # press 'ESC' to exit

    cam.release()
    out.release()
    cv2.destroyAllWindows()
    print('Finished!') # end confirm

testCameras()
# max my webcam can support without losing quality
recordVideo('out.avi', 'XVID', 30.0, 640, 480)
