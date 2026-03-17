import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtCore import Qt


def main():
    app = QApplication(sys.argv)

    window = QWidget()

    window.setWindowFlags(Qt.WindowType.FramelessWindowHint)

    window.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
    #! Makes window click through
    window.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

    label = QLabel(window)

    pixmap = QPixmap('1.png')
    label.setPixmap(pixmap)
    label.setGeometry(0, 0, pixmap.width(), pixmap.height())

    window.resize(pixmap.width(), pixmap.height())
    window.show()

    sys.exit(app.exec())

main()