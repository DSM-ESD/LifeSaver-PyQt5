from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class SeatMonitoring(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 480)
        self.label = QLabel('test', self)
        self.lists = [[0 for j in range(20)] for i in range(5)]
        print(self.lists)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.fillRect(QRect(0, 0, 800, 480), QColor('white'))
        qp.end()
        

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = SeatMonitoring()
    ui.show()
    sys.exit(app.exec_())