import sys
import time
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt, QTimer, QRectF
from PyQt6.QtGui import QPainter, QPen, QColor

from reader import MemoryReader
from utils import getTargetPID, worldToScreen, smoothScreenPositions

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

        screen = QApplication.primaryScreen().geometry()
        self.width = screen.width()
        self.height = screen.height()

        if not fullscreen:
            self.width = int(input("Window width (pixels)?: "))
            self.height = int(input("Window height (pixels)?: "))

        self.resize(self.width, self.height)
        self.move(0, 0)

        self.reader = MemoryReader(pid)
        self.playerDraws = []
        self.cameraInfo = None

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.onData)
        self.timer.start(int(1000 / FPS))

    def onData(self):
        self.playerDraws = self.reader.getPlayers()
        self.cameraInfo = self.reader.getCameraInfo()
        self.update()

    def paintEvent(self, event):
        if not self.playerDraws or not self.cameraInfo:
            return

        painter = QPainter(self)
        pen = QPen(QColor(0, 255, 0, 200))
        pen.setWidth(2)
        painter.setPen(pen)

        for player in self.playerDraws:
            playerID = player['id']
            x, y, z = player['x'], player['y'], player['z']

            feetPosition = {'x': x, 'y': y - 2.5, 'z': z}
            headPosition = {'x': x, 'y': y + 2.5, 'z': z}

            feetScreenLocation = worldToScreen(feetPosition, self.cameraInfo, self.width, self.height)
            headScreenLocation = worldToScreen(headPosition, self.cameraInfo, self.width, self.height)

            if feetScreenLocation and headScreenLocation:
                feetX, feetY, feetDepth = feetScreenLocation
                headX, headY, headDepth = headScreenLocation

                feetX, feetY = smoothScreenPositions("{}_feet".format(playerID), feetX, feetY)
                headX, headY = smoothScreenPositions("{}_head".format(playerID), headX, headY)

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