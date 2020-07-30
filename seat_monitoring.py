from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSvg import *

class SeatMonitoring(QWidget):
    def __init__(self, pager=None):
        super().__init__()
        self.resize(800, 480)
        self.setAttribute(Qt.WA_StyledBackground, True)
        # allow custom wigdet to use style sheet

        self.pager = pager
        self.render = QSvgRenderer('res/bus.svg')
        self.lists = [[0 for j in range(7)] for i in range(3)]
        self.setStyleSheet('background-color: white')
        self.colors = [QColor('gray'), QColor('green'), QColor('red')]

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        cX = 161
        cY = [141,233,289]
        cenY = 240 - (2.5 * 40)
        self.render.render(qp, QRectF(33, 95, 734, 290))
        for i, col in enumerate(self.lists):
            for j, row in enumerate(col):
                rect = QRect(cX + j * 50 + (j) * 37, cY[i], 50, 50)
                qp.fillRect(rect, self.colors[row])
        qp.end()
    
    def mousePressEvent(self, event):
        self.pager.emit(1)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = SeatMonitoring()
    ui.show()
    sys.exit(app.exec_())