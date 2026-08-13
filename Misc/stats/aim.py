import sys
import time
import math
import threading

from PyQt6.QtWidgets import QApplication
from evdev import UInput, ecodes, InputDevice, list_devices

from reader import MemoryReader
from utils import getTargetPID, getWindowSize, worldToScreen

rate = float(1/165.0)
aimActive = False

def listener():
    global aimActive

    for path in list_devices():
        device = InputDevice(path)
        caps = device.capabilities()

        if ecodes.EV_KEY not in caps: continue # perpherials have ev keys
        keys = caps[ecodes.EV_KEY]

        validKeys = [ecodes.KEY_W, ecodes.KEY_A, ecodes.KEY_S, ecodes.KEY_D, ecodes.KEY_SPACE, ecodes.KEY_V]
        if not all(key in keys for key in validKeys): continue # to check if keyboard is valid
        if not "keyboard" in device.name.lower(): continue

        print("Listening for 'V' on keyboard: {}".format(device.name))

        for event in device.read_loop():
            if event.type == ecodes.EV_KEY and event.code == ecodes.KEY_V and event.value == 1:
                aimActive = not aimActive
                print("Aim {}".format('on' if aimActive else 'off'))
        break

def aim(pid):
    mouse = UInput({
        ecodes.EV_REL: (ecodes.REL_X, ecodes.REL_Y),
        ecodes.EV_KEY: (ecodes.BTN_LEFT, ecodes.BTN_RIGHT) # making sure DEs recognize as "mouse"
    }, name='virtual-mus-musculus')
    if mouse: print("Created virtual mouse: {}".format(mouse.name))

    reader = MemoryReader(pid)
    app = QApplication(sys.argv)

    windowDimensions = getWindowSize(pid)
    if windowDimensions:
        x, y, width, height = windowDimensions
    else:
        screen = QApplication.primaryScreen().geometry()
        x, y = 0, 0
        width, height = screen.width(), screen.height()

    centerX = width / 2
    centerY = height / 2
    print(centerX, centerY)

    threading.Thread(target=listener, daemon=True).start()

    while True:
        if not aimActive:
            time.sleep(0.05) # save cpu
            continue

        reader.resolvePointerChain()
        camera = reader.getCameraInfo()
        players = reader.getPlayers()

        if not camera or not players:
            time.sleep(rate)
            continue

        bestTarget = None
        minScreenDistance = float('inf') # learned about this

        for player in players:
            if not player['visible']: continue

            targetPosition = {'x': player['x'], 'y': player['y'] + 1, 'z': player['z']}
            screenPosition = worldToScreen(targetPosition, camera, width, height)

            if screenPosition:
                screenX, screenY, depth = screenPosition

                if depth > 0: # didn't want to do real math so this will suffice to find closest player on screen
                    distance = math.hypot(screenX - centerX, screenY - centerY)

                    if distance < 100 and distance < minScreenDistance: # only snaps when player is within 100 pixels of center
                        minScreenDistance = distance
                        bestTarget = (screenX, screenY)

        if bestTarget:
            targetX, targetY = bestTarget

            dX = targetX - centerX
            dY = targetY - centerY

            moveX = round(dX)
            moveY = round(dY)

            if moveX != 0:
                mouse.write(ecodes.EV_REL, ecodes.REL_X, moveX)
            if moveY != 0:
                mouse.write(ecodes.EV_REL, ecodes.REL_Y, moveY)
            mouse.syn()

        time.sleep(rate)

def main():
    if len(sys.argv) > 1:
        pid = getTargetPID(sys.argv[1])
        aim(pid)
    else:
        print("Add an argument when executing")

if __name__ == "__main__":
    main()