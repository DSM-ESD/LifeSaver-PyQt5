from PyQt5 import QtCore, QtGui, QtWidgets

class SeatMonitoring(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.resize(800, 480)
        self.setStyleSheet('background-color:white;')
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = SeatMonitoring(None)
    ui.show()
    sys.exit(app.exec_())