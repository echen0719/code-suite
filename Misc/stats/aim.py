import sys
import time
import math

from PyQt6.QtWidgets import QApplication
from pynput.mouse import Controller
from pynput.keyboard import Listener as KeyboardListener

from reader import MemoryReader
from utils import getTargetPID, getWindowSize, worldToScreen

rate = 0.0063
aimActive = True

def onToggle(key):
    if key.char == 'v':
        aimActive = not aimActive
        print("Aim {}".format('on' if aimActive else 'off'))

def aim(pid):
    reader = MemoryReader(pid)
    mouse = Controller()
    app = QApplication(sys.argv)

    windowDimensions = () # getWindowSize(pid)
    if windowDimensions:
        x, y, width, height = windowDimensions
    else:
        screen = QApplication.primaryScreen().geometry()
        x, y = 0, 0
        width, height = screen.width(), screen.height()

    centerX = width / 2
    centerY = height / 2

    # mouse listening for snapping purposes
    listener = KeyboardListener(on_click=onToggle)
    listener.start()

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

            mouse.move(int(dX), int(dY))

        time.sleep(rate)

def main():
    if len(sys.argv) > 1:
        pid = getTargetPID(sys.argv[1])
        aim(pid)
    else:
        print("Add an argument when executing")

if __name__ == "__main__":
    main()