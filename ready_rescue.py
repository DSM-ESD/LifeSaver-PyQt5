from PyQt5 import QtGui ,QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Ui_ready_rescue(QtWidgets.QWidget):
    def __init__(self, pager):
        super().__init__()
        self.pager = pager
        self.setObjectName("ready_rescue")
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

        self.label.setObjectName("ready_rescue")
        self.label.setText("\n클릭하면 다음페이지로 넘어갑니다. \n \n")
        self.label.setStyleSheet('background:#1C972F; color: #FFFFFF; font-family: Roboto; font-style: normal;font-weight: bold;font-size: 30px;line-height: 35px; ') # stylesheet background color change
        #취소 버튼
        pybutton = QtWidgets.QPushButton('취소하기 없음',self)
        
        pybutton.resize(250,80)
        pybutton.move(100,360)
        pybutton.setStyleSheet("background: #5E6AD6; color : #FFFFFF; font-size: 27px; line-height: 27px; font-weight : bold; ")
        pybutton2 = QtWidgets.QPushButton(f'요청하기',self)
        pybutton2.resize(250,80)
        pybutton2.move(450,360)
        pybutton2.setStyleSheet("background: #5E6AD6; color : #FFFFFF; font-size: 27px; line-height: 27px; font-weight : bold; ")
        pybutton2.clicked.connect(self.movePage)
    
    def movePage(self, event):
        self.pager.emit(1)



        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rescueReqestpage = QtWidgets.QWidget()
    ui = Ui_ready_rescue()
    ui.setupUi(rescue_1)
    rescueReqestpage.show()
    sys.exit(app.exec_())
