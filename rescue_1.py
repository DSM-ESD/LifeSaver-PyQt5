from PyQt5 import QtGui ,QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from time import sleep

class Ui_rescue_1(QtWidgets.QWidget):
    def __init__(self, pager):
        super().__init__()
        self.pager = pager
        self.time = 20
        self.g_Flag = True

        self.setObjectName("rescue_1")
        self.resize(800,480)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(100,60,600,250)) # label (x,y,width,heigh)
        self.label2 = QtWidgets.QLabel(self)
        self.label2.setGeometry(QtCore.QRect(100,210,600,75))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setFont(font)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        # label
        self.label2.setObjectName("rescue_1")
        self.label.setObjectName("rescue_1")
        self.label.setText("사고가 감지되었습니다.\n 구조요청을 진행하시겠습니까?\n\n")
        self.label.setStyleSheet('background:#1C972F; color: #FFFFFF; font-family: Roboto; font-style: normal;font-weight: bold;font-size: 30px;line-height: 35px; ') # stylesheet background color change
        self.label2.setText("20초간 응답이 없을 시 자동으로 요청됩니다.")
        self.label2.setStyleSheet('background:#1C972F; color: #FFFFFF; font-family: Roboto; font-style: normal;font-weight: bold;font-size: 27px;line-height: 35px; ') # stylesheet background color change

        #취소 버튼
        self.pybutton = QtWidgets.QPushButton('취소',self)
        self.pybutton.resize(250,80)
        self.pybutton.move(100,360)
        self.pybutton.setStyleSheet("background: #5E6AD6; color : #FFFFFF; font-size: 27px; line-height: 27px; font-weight : bold; ")
        self.pybutton.clicked.connect(lambda x: self.movePage(0))

        self.pybutton2 = QtWidgets.QPushButton(f'요청..20',self)
        self.pybutton2.resize(250,80)
        self.pybutton2.move(450,360)
        self.pybutton2.setStyleSheet("background: #5E6AD6; color : #FFFFFF; font-size: 27px; line-height: 27px; font-weight : bold; ")

    def movePage(self, index):
        if index == 0:
            self.g_Flag = False
        self.pager.emit(index)
        
        
    def CountTime(self):
        self.g_Flag = True
        self.time = 20
        while self.time > 0 and self.g_Flag:
            self.time -= 1
            self.pybutton2.setText(f"요청..{self.time}")
            
            sleep(1)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rescueReqestpage = QtWidgets.QWidget()
    ui = Ui_rescueReqestpage()
    ui.setupUi(rescue_1)
    rescueReqestpage.show()
    sys.exit(app.exec_())
