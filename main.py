from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from rescue_1 import *
from ready_rescue import *
import threading

class Main(QtWidgets.QStackedWidget):
    pager = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.pager.connect(self.changePageEvent)
        self.resize(800,480)
        self.addWidget(Ui_ready_rescue(self.pager))
        self.addWidget(Ui_rescue_1(self.pager))
        
    
    def changePageEvent(self, index):
        self.setCurrentIndex(index)
        if index == 1:
            self.th = threading.Thread(target = self.widget(1).CountTime)
            self.th.daemon = True
            self.th.start()
        else:
            self.th.join()
            self.th = None


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    ui.setCurrentIndex(0)
    app.exec_()