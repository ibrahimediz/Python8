import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button'
        self.left = 20
        self.top = 20
        self.width = 320
        self.height = 200
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        button = QPushButton('PyQt5 1 button', self)
        button.setToolTip('Birinci Buton')
        button.move(100,70)
        button.clicked.connect(self.on_click1)
        button1 = QPushButton("PyQt5 2 buton",self)
        button1.setToolTip("İkinci Button")
        button1.move(150, 80)
        button1.clicked.connect(self.on_click1)
        self.show()
    @pyqtSlot()
    def on_click1(self):
        print('Birinci Buton click')
    def on_click2(self):
        print("İkici Buton click")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())