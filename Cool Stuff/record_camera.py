import cv2

cameraIndex = int(input('Which camera are you using (0 for main, 1 for secondary, and so on)?: '))

cam = cv2.VideoCapture(cameraIndex, cv2.CAP_DSHOW)
if not cam.isOpened():
    print("Cannot open webcam")
    exit

# https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html

def exitCV():
    cam.release()
    cv2.destroyAllWindows()

def recordVideo(fileName, vidFormat, fps, sizeX, sizeY):
    out = cv2.VideoWriter(fileName, cv2.VideoWriter_fourcc(*vidFormat), fps, (sizeX, sizeY))
    while cam.isOpened():
        success, frame = cam.read()
        if not success: break
        cv2.imshow('Camera Feed Window', frame)
        out.write(frame)
        if cv2.waitKey(1) == 27: break # press 'ESC' to exit

    out.release()
    exitCV()

print('Started!')
#recordVideo('out.mp4', 'XVID', 30.0, 1280, 720)
recordVideo('out.avi', 'DIVX', 30.0, 1280, 720)
print('Finished!')
