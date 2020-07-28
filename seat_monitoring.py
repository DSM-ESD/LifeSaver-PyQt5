from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from random import *

class SeatMonitoring(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 480)
        self.lists = [[randrange(0,3) for j in range(10 if i != 2 else 1)] for i in range(5)]
        self.colors = [QColor('gray'), QColor('green'), QColor('red')]
        print(self.lists)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.fillRect(0, 0, 800, 480, QColor('white'))
        for i, col in enumerate(self.lists):
            for j, row in enumerate(col):
                qp.fillRect(j * 50, i * 50, 30, 30, self.colors[row])

        qp.end()
        

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = SeatMonitoring()
    ui.show()
    sys.exit(app.exec_())