from PyQt5 import QtCore, QtGui, QtWidgets

class Main(QtWidgets.QStackedWidget):
    def __init__(self):
        super().__init__()
        self.resize(800,480)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    ui.setCurrentIndex(2)
    app.exec_()