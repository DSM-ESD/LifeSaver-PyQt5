from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from math import cos, pi
from threading import Thread
from time import sleep

class RescueRequest(QWidget):
    def __init__(self, pager = None):
        super().__init__()
        self.pager = pager # 페이지 이동 pager
        self.time = 20 # tiem 초기화
        self.flag = True # 기본으로 thread 켜기
        
        self.resize(800,480)
        self.th = None
        self.label = QLabel(self)
        self.label.setGeometry(QRect(100,60,600,250)) # label (x,y,width,heigh)
        self.label2 = QLabel(self)
        self.label2.setGeometry(QRect(100,210,600,75))
        
        # label
        self.label.setText("사고가 감지되었습니다.\n구조요청을 진행하시겠습니까?\n\n")
        self.label.setStyleSheet('background:#1C972F; color: #FFFFFF; font: 25pt \"나눔스퀘어 Bold\";')
        self.label.setAlignment(Qt.AlignCenter)
        self.label2.setText("20초간 응답이 없을 시 자동으로 요청됩니다.")
        self.label2.setStyleSheet('background:#1C972F; color: #FFFFFF; font: 20pt \"나눔스퀘어\";')
        self.label2.setAlignment(Qt.AlignCenter)

        #취소 버튼
        self.cancelBtn = QPushButton('취소',self)
        self.cancelBtn.resize(250,80)
        self.cancelBtn.move(100,360)
        self.cancelBtn.setStyleSheet('background: #5E6AD6; color: #FFFFFF; font: 20pt \"나눔스퀘어 Bold\"; border-radius: 0px')
        self.cancelBtn.clicked.connect(lambda: self.pager.emit(0))

        self.requestBtn = QPushButton(f'요청..20',self) # 요청 버튼
        self.requestBtn.resize(250,80)
        self.requestBtn.move(450,360)
        self.requestBtn.setStyleSheet('background: #5E6AD6; color: #FFFFFF; font: 20pt \"나눔스퀘어 Bold\"; border-radius: 0px')
        self.requestBtn.clicked.connect(lambda: self.pager.emit(2))
        self.background = QColor('red')

    def onPaging(self, idx):
        if idx == 1:
            self.th = Thread(target=self.CountTime, args=())
            self.th.daemon = True
            self.flag = True
            self.th.start()
        else:
            if self.th:
                self.flag = False
                self.th.join()
                self.th = None
                self.requestBtn.setText('요청..20')
                self.background.setAlpha(255)

        
    def paintEvent(self, e):
        painter = QPainter(self)
        painter.fillRect(0,0,800,480,self.background)
        painter.end()

    def CountTime(self): # 1초 slepp함수
        cnt = 0
        theta = 0
        level = 0
        self.flag = True
        self.time = 20
        while self.time > 0: # tiem이 0보다 크면서 g_Flag가 Treu 이면
            if cnt > 50:
                cnt = 0
                self.time -= 1 # tiem 1씩 감소
                self.requestBtn.setText(f"요청..{self.time}") # 버튼 텍스트 바꾸기
            level = int(cos((theta * pi / 180) * 10) * 127.5 + 127.5)
            theta += 1
            cnt += 1
            self.background.setAlpha(level)
            self.update()
            if not self.flag:
                return
            sleep(0.02)  # 20ms간 딜레이
        self.pager.emit(2)


            
   



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = RescueRequest()
    ui.show()
    sys.exit(app.exec_())

