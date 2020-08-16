from PyQt5 import QtCore, QtGui, QtWidgets
from SeatMonitoring import *
from RescueRequest import *
from RescueFinished import *

class Main(QtWidgets.QStackedWidget):
    pager = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.resize(800,480)
        self.pager.connect(self.setCurrentIndex)

        monitoring = SeatMonitoring(self.pager)
        self.addWidget(monitoring)

        requset = RescueRequest(self.pager)
        self.currentChanged.connect(requset.onPaging)
        self.addWidget(requset)

        finished = RescueFinished(self.pager)
        self.addWidget(finished)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    ui.setCurrentIndex(0)
    app.exec_()
