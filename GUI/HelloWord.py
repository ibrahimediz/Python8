import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
class App(QWidget):
     def __init__(self):
        super().__init__()
        self.title = 'PyQt5 örnek window'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
     def initUI(self):
        self.setWindowTitle(self.title)
        text = QLabel("Merhaba",self)
        text.setAlignment(Qt.AlignCenter)
        text.setStyleSheet("color: rgb(0,0,255);font-weight: bold; font-size: 16pt")
        text.setText("merhaba PyQt5")
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = App()
   sys.exit(app.exec_())