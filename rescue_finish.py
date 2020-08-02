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
        self.label.setGeometry(QtCore.QRect(100,60,600,380)) # label (x,y,width,heigh)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        
    

        # label
        self.label.setObjectName("rescue_finish")
        self.label.setText("긴급 구조 요청을\n성공적으로 진행하였습니다.\n\n버스 기사님께서는 승객의\n상태를 확인하여 주시길 바랍니다.")
        self.label.setStyleSheet('background:#1C972F; color: #FFFFFF; font-family: Roboto; font-style: normal;font-weight: bold;font-size: 30px;line-height: 35px; ') # stylesheet background color change
   
    
    def mousePressEvent(self, event):
        self.pager.emit(0)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rescueReqestpage = QtWidgets.QWidget()
    ui = Ui_rescue_finish()
    ui.setupUi(rescue_1)
    rescueReqestpage.show()
    sys.exit(app.exec_())
