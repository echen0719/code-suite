import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt, QTimer, QRectF
from PyQt6.QtGui import QPainter, QPen, QColor

from reader import MemoryReader
from utils import getTargetPID, worldToScreen

class Overlay(QWidget):
    def __init__(self, pid):
        super().__init__()
        fullscreen = True
        FPS = 165

        # prevent from interferring
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        # stay on top, transparent (remember to set "Keep Above Others" in Wayland)
        self.setWindowFlags(
            Qt.WindowType.Window | Qt.WindowType.Tool |
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

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateFrame)
        self.timer.start(int(1000 / FPS))

        self.playerDraws = []

    def updateFrame(self):
        players = self.reader.getPlayers()

        cameraInfo = self.reader.getCameraInfo()
        if not cameraInfo:
            self.playerDraws = []
            self.update()
            return

        self.playerDraws = []
        for playerPosition in players:
            screenCoordinates = worldToScreen(playerPosition, cameraInfo, self.width, self.height, fov=90.0)

            if screenCoordinates:
                x, y, depth = screenCoordinates

                if -100 < x < self.width + 100 and -100 < y < self.height + 100: # make sure player is visible on screen
                    self.playerDraws.append({'x': x, 'y': y, 'depth': depth})
        self.update()

    def paintEvent(self, event):
        if not self.playerDraws:
            return

        painter = QPainter(self)
        pen = QPen(QColor(0, 255, 0, 200))
        pen.setWidth(2)
        painter.setPen(pen)

        for player in self.playerDraws:
            # reference for game meters to pixels
            boxHeight = max(20.0, 150.0 * (5.0 / (player['depth'] + 1.0)))
            boxWidth = boxHeight * 0.4

            topLeftX = player['x'] - (boxWidth / 2.0)
            topLeftY = player['y'] - boxHeight

            painter.drawRect(QRectF(topLeftX, topLeftY, boxWidth, boxHeight))
        painter.end()

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