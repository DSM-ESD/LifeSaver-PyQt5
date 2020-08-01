from PyQt5 import QtGui ,QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Ui_rescue_finish(QtWidgets.QWidget):
    def __init__(self, pager):
        super().__init__()
        self.pager = pager

        self.setObjectName("rescue_finish")
        self.resize(800,480)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(100,60,600,250)) # label (x,y,width,heigh)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        
       
        # label
      
        self.label.setObjectName("rescue_finish")
        self.label.setText("구조요청 신호가 \n 정상적으로 보내졌습니다. \n")
        self.label.setStyleSheet('background:#1C972F; color: #FFFFFF; font-family: Roboto; font-style: normal;font-weight: bold;font-size: 30px;line-height: 35px; ') # stylesheet background color change
       
        #돌아가기 버튼
        pybutton = QtWidgets.QPushButton('처음으로 돌아가기',self)        
        pybutton.resize(600,80)
        pybutton.move(100,360)
        pybutton.setStyleSheet("background: #5E6AD6; color : #FFFFFF; font-size: 27px; line-height: 27px; font-weight : bold; ")
        
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rescueReqestpage = QtWidgets.QWidget()
    ui = Ui_rescue_finish()
    ui.setupUi(rescue_1)
    rescueReqestpage.show()
    sys.exit(app.exec_())
