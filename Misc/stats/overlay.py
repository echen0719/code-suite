import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor

from reader import MemoryReader
from utils import getTargetPID, worldToScreen

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

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush(QColor(255, 255, 255, 20)))
        painter.drawRect(0, 0, self.width, self.height)

def main():
    app = QApplication(sys.argv) # pass in environmental variables
    overlay = Overlay(67)
    overlay.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()