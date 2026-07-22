import sys
import time
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt, QTimer, QRectF, QThread, pyqtSignal
from PyQt6.QtGui import QPainter, QPen, QColor

from reader import MemoryReader
from utils import getTargetPID, worldToScreen

# separate thread for performance and safety
class ReaderThread(QThread):
    dataSend = pyqtSignal(list, dict)

    def __init__(self, reader):
        super().__init__()
        self.reader = reader
        self.running = True
        self.FPS = 165

    def run(self):
        while self.running:
            players = self.reader.getPlayers()
            camera = self.reader.getCameraInfo()

            self.dataSend.emit(players, camera)
            time.sleep(1 / self.FPS)

    def stop(self):
        self.running = False
        self.wait()

class Overlay(QWidget):
    def __init__(self, pid):
        super().__init__()
        fullscreen = True

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
        self.playerDraws = []
        self.cameraInfo = None

        self.thread = ReaderThread(self.reader)
        self.thread.dataSend.connect(self.onData)
        self.thread.start()

    def onData(self, playerDraws, cameraInfo):
        self.playerDraws = playerDraws
        self.cameraInfo = cameraInfo
        self.update()

    def paintEvent(self, event):
        if not self.playerDraws or not self.cameraInfo:
            return

        painter = QPainter(self)
        pen = QPen(QColor(0, 255, 0, 200))
        pen.setWidth(2)
        painter.setPen(pen)

        for player in self.playerDraws:
            feetPosition = {'x': player['x'], 'y': player['y'], 'z': player['z']}
            headPosition = {'x': player['x'], 'y': player['y'] + 2, 'z': player['z']}

            feetScreenLocation = worldToScreen(feetPosition, self.cameraInfo, self.width, self.height, fov=90.0)
            headScreenLocation = worldToScreen(headPosition, self.cameraInfo, self.width, self.height, fov=90.0)

            if feetScreenLocation and headScreenLocation:
                feetX, feetY, feetDepth = feetScreenLocation
                headX, headY, headDepth = headScreenLocation

                boxHeight = feetY - headY
                if boxHeight <= 0: continue

                boxWidth = boxHeight * 0.5
                painter.drawRect(QRectF(headX - boxWidth / 2, headY, boxWidth, boxHeight))

    def closeEvent(self, event):
        self.thread.stop()
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