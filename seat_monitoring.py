from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSvg import *
from sub_widgets.Button import Button

class SeatMonitoring(QWidget):
    def __init__(self, pager=None):
        super().__init__()
        self.resize(800, 480)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.pager = pager
        self.bus = QSvgRenderer('res/bus.svg')
        self.lists = [[0 for j in range(7)] for i in range(3)]
        self.setStyleSheet('SeatMonitoring { background-color: white }')
        self.colors = [QColor(192,192,192), QColor('green'), QColor('red')]
        self.createWidgets()

    def createWidgets(self):
        self.requestBtn = Button('수동 구조 요청', self)
        self.requestBtn.setGeometry(400,400,200,80)
        self.settingBtn = Button('설정', self)
        self.settingBtn.setGeometry(601,400,200,80)

    def paintEvent(self, event):
        qp = QPainter(self)
        cX = 161
        cY = [141, 233, 289]
        self.bus.render(qp, QRectF(33, 95, 734, 290))
        for i, col in enumerate(self.lists):
            for j, row in enumerate(col):
                rect = QRect(cX + j * 87, cY[i], 50, 50)
                qp.fillRect(rect, self.colors[row])
        qp.drawLine(0, 399, 800, 399)
        qp.drawLine(600, 399, 600, 480)
        qp.end()
    

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = SeatMonitoring()
    ui.show()
    sys.exit(app.exec_())
