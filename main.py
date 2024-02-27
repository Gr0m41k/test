import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from random import randint


def draw_circles(qp):
    qp.setBrush(QColor('yellow'))
    x = y = randint(30, 180)
    qp.drawEllipse(360, 250, x, y)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('untitleddd.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter(self.centralwidget)
            qp.begin(self)
            draw_circles(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


