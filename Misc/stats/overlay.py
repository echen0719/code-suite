import sys
import time
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt, QTimer, QRectF
from PyQt6.QtGui import QPainter, QPen, QColor

from reader import MemoryReader
from utils import getTargetPID, getWindowSize, worldToScreen, smoothCamera, smooth3D

class Overlay(QWidget):
    def __init__(self, pid):
        super().__init__()
        fullscreen = True
        FPS = 165

        # stay on top, transparent (remember to set "Keep Above Others" in Wayland)
        self.setWindowFlags(
            Qt.WindowType.Tool |
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.WindowDoesNotAcceptFocus |
            Qt.WindowType.WindowTransparentForInput |
            Qt.WindowType.X11BypassWindowManagerHint
        )

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating)

        windowDimensions = () # getWindowSize(pid)
        if windowDimensions:
            self.x, self.y, self.width, self.height = windowDimensions
        else:
            screen = QApplication.primaryScreen().geometry()
            self.x, self.y = 0, 0
            self.width, self.height = screen.width(), screen.height()

        self.resize(self.width, self.height)
        self.move(self.x, self.y)

        self.reader = MemoryReader(pid)
        self.reader.resolvePointerChain()
        self.playerDraws = []
        self.cameraInfo = None

        self.timer = QTimer(self)
        self.timer.setTimerType(Qt.TimerType.PreciseTimer)
        self.timer.timeout.connect(self.onData)
        self.timer.start(int(1000 / FPS))

    def onData(self):
        self.playerDraws = self.reader.getPlayers()
        self.cameraInfo = self.reader.getCameraInfo()
        self.repaint()

    def paintEvent(self, event):
        if not self.playerDraws or not self.cameraInfo:
            return

        painter = QPainter(self)
        pen = QPen(QColor(0, 255, 0, 200))
        pen.setWidth(2)
        painter.setPen(pen)

        currentTime = time.time()
        # smoothedCamera = smoothCamera(self.cameraInfo, currentTime)

        for player in self.playerDraws:
            playerID = player['id']
            x, y, z = player['x'], player['y'], player['z']

            smoothX, smoothY, smoothZ = smooth3D(playerID, x, y, z, currentTime)

            feetPosition = {'x': smoothX, 'y': smoothY - 2, 'z': smoothZ}
            headPosition = {'x': smoothX, 'y': smoothY + 3, 'z': smoothZ}

            feetScreenLocation = worldToScreen(feetPosition, self.cameraInfo, self.width, self.height)
            headScreenLocation = worldToScreen(headPosition, self.cameraInfo, self.width, self.height)

            if feetScreenLocation and headScreenLocation:
                feetX, feetY, feetDepth = feetScreenLocation
                headX, headY, headDepth = headScreenLocation

                boxHeight = feetY - headY
                if boxHeight <= 0: continue

                boxWidth = boxHeight * 0.5
                painter.drawRect(QRectF(headX - boxWidth / 2, headY, boxWidth, boxHeight))

    def closeEvent(self, event):
        self.timer.stop()
        self.reader.close()
        super().closeEvent(event)

def main():
    if len(sys.argv) > 1:
        app = QApplication(sys.argv) # pass in environmental variables
        overlay = Overlay(getTargetPID(sys.argv[1]))
        overlay.show()
        sys.exit(app.exec())
    else:
        print("Add an argument when executing")

if __name__ == "__main__":
    main()