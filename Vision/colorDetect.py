import cv2
from PIL import Image
import numpy as np
import platform

platform = platform.system()

# dictionary of colors
# https://stackoverflow.com/questions/36817133/identifying-the-range-of-a-color-in-hsv-using-opencv

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

# dictionary of common colors in numpy array form

colorLimits = {
'red': [(np.array([0, 100, 100], dtype=np.uint8), np.array([10, 255, 255], dtype=np.uint8)), (np.array([170, 100, 100], dtype=np.uint8), np.array([180, 255, 255], dtype=np.uint8))],
'orange': [(np.array([10, 100, 100], dtype=np.uint8), np.array([25, 255, 255], dtype=np.uint8))],
'yellow': [(np.array([25, 100, 100], dtype=np.uint8), np.array([35, 255, 255], dtype=np.uint8))],
'green': [(np.array([35, 50, 50], dtype=np.uint8), np.array([85, 255, 255], dtype=np.uint8))],
'blue': [(np.array([100, 100, 100], dtype=np.uint8), np.array([140, 255, 255], dtype=np.uint8))],
'violet': [(np.array([130, 50, 50], dtype=np.uint8), np.array([160, 255, 255], dtype=np.uint8))],
'black': [(np.array([0, 0, 0], dtype=np.uint8), np.array([180, 255, 50], dtype=np.uint8))],
'white': [(np.array([0, 0, 200], dtype=np.uint8), np.array([180, 50, 255], dtype=np.uint8))]
}

def detectColors(color, exposure):
    colorRange = colorLimits[color]
    if not colorRange:
        print("Color {color} not found!".format(color))
        exit
        
    cameraIndex = int(input('Which camera are you using (0 for main, 1 for secondary, and so on)?: '))
    cam = createCamera(cameraIndex)

    cam.set(cv2.CAP_PROP_EXPOSURE, exposure)

    print('Started!') # start confirm

    while cam.isOpened():
        success, frame = cam.read()
        if not success: break

        # convert from BGR to HSV using built-in function
        hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsvImage)
        v = cv2.equalizeHist(v)
        hsvImage = cv2.merge((h, s, v))
        # equalizing the value gives better results

        mask = None
        for lower, upper in colorRange:
            preMask = cv2.inRange(hsvImage, lower, upper)
            if mask is None: mask = preMask
            else: mask = cv2.bitwise_or(mask, preMask)

        # I could use masking but I think countour is better
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if cv2.contourArea(contour) > 1000:
                x, y, w, h  = cv2.boundingRect(contour)
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # I kind of know what this does

        cv2.imshow('Mask Feed Window', mask)
        # cv2.imshow('Color Feed Window', frame)
        if cv2.waitKey(1) == 27: break

    cam.release()
    cv2.destroyAllWindows()

choice = input('Choices: red, orange, yellow, green, blue, violet, white, black: ')
print("Using color: {}".format(choice))
detectColors(choice, -5) # need more experimental data
