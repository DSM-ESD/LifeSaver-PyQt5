from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class RescueFinished(QWidget):
    def __init__(self, pager=None):
        super().__init__()
        self.pager = pager
        self.resize(800,480)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('RescueFinished { background-color: white }')

        self.label = QLabel(self)
        self.label.setGeometry(100,60,600,360)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText("긴급 구조 요청을\n성공적으로 진행하였습니다.\n\n버스 기사님께서는 승객의\n상태를 확인하여 주시길 바랍니다.")
        self.label.setStyleSheet('background:#1C972F; color: #FFFFFF; font: 24pt 나눔스퀘어; ') # stylesheet background color change
   
    
    def mousePressEvent(self, event):
        self.pager.emit(0)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = RescueFinished()
    ui.show()
    sys.exit(app.exec_())
