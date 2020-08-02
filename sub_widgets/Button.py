from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt

class Button(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('Button { background-color: #5E6AD6; border: 0px; font: 75 14pt "나눔스퀘어 Bold"; color: white}')
        

