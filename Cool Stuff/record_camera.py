import cv2

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("Cannot open webcam")
    exit

# https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html

def recordVideo(fileName, vidFormat, fps, sizeX, sizeY):
    out = cv2.VideoWriter(fileName, cv2.VideoWriter_fourcc(*vidFormat), fps, (sizeX, sizeY))
    while True:
        success, frame = cam.read()
        if not success: break
        out.write(frame)
        cv2.imshow('Camera Feed Window', frame)
        if cv2.waitKey(1) == 27: break # press 'ESC' to exit

    out.release()
    exitCV()

def exitCV():
    cam.release()
    cv2.destroyAllWindows()

recordVideo('out.avi', 'DIVX', 30.0, 1280, 720)
print('Finished!')
