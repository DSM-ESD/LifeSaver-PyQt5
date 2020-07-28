from PyQt5 import QtCore, QtGui, QtWidgets
from seat_monitoring import *

class Main(QtWidgets.QStackedWidget):
    pager = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.resize(800,480)
<<<<<<< HEAD
        self.pager.connect(self.setCurrentIndex)

        self.addWidget(SeatMonitoring(self.pager))
        self.addWidget(QPushButton())


=======
        self.addWidget(SeatMonitoring())

>>>>>>> b263c8f27773fb671da968f63e57a2ed9a09ac25

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    ui.setCurrentIndex(0)
    app.exec_()