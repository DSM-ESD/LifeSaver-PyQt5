from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
from welcomepage import *
from rescueRequestpage import *
from rescue_1 import *

class Main(QtWidgets.QStackedWidget):
    pager = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.pager.connect(self.setCurrentIndex) # 페이지 이동
        self.resize(800,480)
        self.addWidget(Ui_WelcomePage())
        self.addWidget(Ui_rescueRequestpage(self.pager))
        self.addWidget(Ui_rescue_1())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    ui.setCurrentIndex(1)
    app.exec_()