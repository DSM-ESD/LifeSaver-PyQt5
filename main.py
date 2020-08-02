from PyQt5 import QtCore, QtGui, QtWidgets
from seat_monitoring import *

class Main(QtWidgets.QStackedWidget):
    pager = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.resize(800,480)
        self.pager.connect(self.setCurrentIndex)
        self.addWidget(SeatMonitoring(self.pager))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    ui.setCurrentIndex(0)
    app.exec_()
