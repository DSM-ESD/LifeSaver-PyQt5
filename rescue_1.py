from PyQt5 import QtGui ,QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from time import sleep

class Ui_rescue_1(QtWidgets.QWidget):
    def __init__(self, pager):
        super().__init__()
        self.pager = pager # 페이지 이동 pager
        self.time = 20 # tiem 초기화
        self.g_Flag = True # 기본으로 thread 켜기
        
        self.mainFrame = QtWidgets.QFrame(self)
        self.mainFrame.setGeometry(QtCore.QRect(0,0,800,480)) # label (x,y,width,heigh)


        self.setObjectName("rescue_1")
        
        self.resize(800,480)
        self.label = QtWidgets.QLabel(self.mainFrame)
        self.label.setGeometry(QtCore.QRect(100,60,600,250)) # label (x,y,width,heigh)
        self.label2 = QtWidgets.QLabel(self.mainFrame)
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
        self.pybutton = QtWidgets.QPushButton('취소',self.mainFrame)
        self.pybutton.resize(250,80)
        self.pybutton.move(100,360)
        self.pybutton.setStyleSheet("background: #5E6AD6; color : #FFFFFF; font-size: 27px; line-height: 27px; font-weight : bold; ")
        self.pybutton.clicked.connect(lambda x: self.movePage(0))

        self.pybutton2 = QtWidgets.QPushButton(f'요청..20',self.mainFrame) # 요청 버튼
        self.pybutton2.resize(250,80)
        self.pybutton2.move(450,360)
        self.pybutton2.setStyleSheet("background: #5E6AD6; color : #FFFFFF; font-size: 27px; line-height: 27px; font-weight : bold; ")
        self.pybutton2.clicked.connect(lambda x: self.movePage(2))
        self.mainFrame.setStyleSheet("background-color:rgba(255,0,0,100%);") # 색깔 투명도


    def movePage(self, index):
        if index != 1: # 1이 아니면
            self.g_Flag = False
        self.pager.emit(index)
        
        
    def CountTime(self): # 1초 slepp함수
        self.g_Flag = True
        self.time = 20
        while self.time > 0 and self.g_Flag: # tiem이 0보다 크면서 g_Flag가 Treu 이면
            self.time -= 1 # tiem 1씩 감소
            self.pybutton2.setText(f"요청..{self.time}") # 버튼 텍스트 바꾸기
            sleep(1)  # 1초간 딜레이
            if self.time % 2 == 0:
                self.mainFrame.setStyleSheet("background-color:rgba(255,0,0,100%);") # 색깔 투명도
            else:
                self.mainFrame.setStyleSheet("background-color:rgba(255,0,0,50%);") # 색깔 투명도
        if self.time <= 0:
            self.movePage(2) # 다음 페이지로 이동
            
   



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rescueReqestpage = QtWidgets.QWidget()
    ui = Ui_rescueReqestpage()
    ui.setupUi(rescue_1)
    rescueReqestpage.show()
    sys.exit(app.exec_())
