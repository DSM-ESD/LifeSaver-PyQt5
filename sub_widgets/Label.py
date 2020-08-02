from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

class Label(QLabel):
    def __init__(self, text, parent=None, size=15, color='black'):
        super().__init__(text, parent)
        self.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('Label { background-color: #00000000;font: 75 %dpt "나눔스퀘어"; color: %s}' % (size, color))