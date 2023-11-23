import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor


class CircleDrawer(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()
        self.circles = []

    def initUI(self):
        self.setGeometry(100, 100, 1000, 1000)
        self.setWindowTitle('Circle Drawer')

        self.pushButton.clicked.connect(self.drawCircle)

    def drawCircle(self):
        x = random.randint(0, self.width())
        y = random.randint(0, self.height())
        radius = random.randint(10, 100)

        self.circles.append((x, y, radius))
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawCircles(qp)
        qp.end()

    def drawCircles(self, qp):
        for circle in self.circles:
            x, y, radius = circle
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(x - radius, y - radius, 2 * radius, 2 * radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = CircleDrawer()
    mainWindow.show()
    sys.exit(app.exec_())