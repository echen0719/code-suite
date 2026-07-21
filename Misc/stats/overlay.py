import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor

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
        self.timer.start(int(1 / FPS))

        self.playerDraws = []

    def updateFrame(self):
        players = self.reader.getPlayers()

        cameraInfo = self.reader.getCameraInfo()
        if not cameraInfo:
            self.playerDraws = []
            self.update()
            return

        self.playerDraws = []
        for player in players:
            screenCoordinates = worldToScreen(playerPosition, cameraInfo, self.screen_width, self.screen_height, fov=90.0)

            if screenCoordinates:
                x, y, depth = screenCoordinates

                if -100 < x < self.width + 100 or -100 < y < self.height + 100: # make sure player is visible on screen
                    self.playerDraws.append({'x': x, 'y': y, 'depth': depth})
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush(QColor(255, 255, 255, 20)))
        painter.drawRect(0, 0, self.width, self.height)

def main():
    app = QApplication(sys.argv) # pass in environmental variables
    overlay = Overlay(1141)
    overlay.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()