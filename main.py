import math
import pyautogui
import sys

from enum import Enum

from PyQt6.QtGui import QPixmap, QCursor
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtCore import Qt, QTimer, QPoint

# Screen dimensions
screen_width, screen_height = pyautogui.size()

class Directions(Enum):
    RIGHT = ['1.png', '2.png']
    LEFT = ['3.png', '4.png']

class Snail(QWidget):
    def __init__(self):
        super().__init__()

        # Window settings
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

        # Point/Pos
        self.point = QPoint()

        # Snail attributes
        self.sprite = 0
        self.count = 0

        # Label
        self.label = QLabel(self)

        # Timer for animation
        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(100)  # update every 100ms

    def animate(self):
        self.count += 1

        if self.count >= 5:
            self.count = 0
            self.sprite = 1 if self.sprite == 0 else 0

        self.updatePos()

        if self.distanceX < 0:
            direction = Directions.LEFT
        else:
            direction = Directions.RIGHT

        img = direction.value[self.sprite]
        self.updateImg(img)

    def updatePos(self):
        ## Follow mouse
        mouse_pos = QCursor.pos()

        #? Get direction/distance of mouse
        self.geo = self.geometry() # This gets pos and size
        # print(geo.x(), geo.y(), geo.width(), geo.height())

        #* Calculate distance
        self.distanceX = mouse_pos.x() - self.geo.x() # if positive then move right, if negative then left
        self.distanceY = mouse_pos.y() - self.geo.y() # if positve then move down, if negative then move up
        distance = math.hypot(self.distanceX,self.distanceY)

        if distance < 5:
            return

        speed = 8
        #  direction vector
        velocoityX = (self.distanceX / distance) * speed
        velocoityY = (self.distanceY / distance) * speed

        new_x = self.geo.x() + velocoityX
        new_y = self.geo.y() + velocoityY

        self.move(int(new_x), int(new_y))

    def updateImg(self, img):
        pixmap = QPixmap(img)

        self.label.setPixmap(pixmap)
        self.label.setGeometry(0, 0, pixmap.width(), pixmap.height())

        self.resize(pixmap.width(), pixmap.height())


# RUN
if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = Snail()
    win.show()

    sys.exit(app.exec())