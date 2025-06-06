import os
os.environ['OPENCV_LOG_LEVEL'] = 'SILENT'
# stop warnings that fill console
import cv2
import platform

# https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html

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

colorInfo, fontColor, textX, textY = "", (0, 0, 0), 0, 0
# I think this is one way to do it

def getColorOnMouseClick(event, x, y, flags, param):
    global colorInfo, fontColor, textX, textY
    
    if event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = param[y, x] # turns out y, x will give correct value, not the other way around
        textX, textY = x, y
        fontColor = (int(255 - b), int(255 - g), int(255 - r)) # inverted
        colorInfo = '({}, {}): rgb({}, {}, {}) | #{:02x}{:02x}{:02x}'.format(x, y, r, g, b, r, g, b)

def recordVideo():
    global colorInfo, fontColor, textX, textY
    
    cameraIndex = int(input('Which camera are you using (0 for main, 1 for secondary, and so on)?: '))
    cam = createCamera(cameraIndex)

    cv2.namedWindow('Video Feed Window')
    cv2.setMouseCallback('Video Feed Window', getColorOnMouseClick)
    
    while cam.isOpened():
        success, frame = cam.read()
        if not success: break
        cv2.setMouseCallback('Video Feed Window', getColorOnMouseClick, param=frame)
        # supposedly, this will cut number of iterations
        if colorInfo: # this works well but I need to fix it when text goes outside the boundaries
            cv2.putText(frame, colorInfo, (textX + 10, textY + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, fontColor, 2)
        cv2.imshow('Video Feed Window', frame)
        if cv2.waitKey(1) == 27: break # press 'ESC' to exit

    cam.release()
    cv2.destroyAllWindows()
    print('Finished!') # end confirm

testCameras()
recordVideo()