from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor
from rescue_1 import *
from ready_rescue import *
from rescue_finish import *
import threading

class Main(QtWidgets.QStackedWidget):
    pager = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color : grb(10,50,100);")
        self.pager.connect(self.changePageEvent) #pager 연결되면 함수불러오기
        self.resize(800,480)
        self.addWidget(Ui_ready_rescue(self.pager)) # index 0
        self.addWidget(Ui_rescue_1(self.pager)) #index 1
        self.addWidget(Ui_rescue_finish(self.pager)) #index 2

    
    def changePageEvent(self, index): #changeEvent
        self.setCurrentIndex(index) # 페이지 이동할 index로 페이지 이동
        if index == 1: # 만약 페이지가 1이면(구조요청 페이지)
            self.th = None # 아니면 끄기
            self.th = threading.Thread(target = self.widget(1).CountTime) #thread 위젯1일때 계속 실행
            self.th.daemon = True
            self.th.start() # thread 시작
            
        else:
            self.th.join()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    ui.setCurrentIndex(0)
    app.exec_()