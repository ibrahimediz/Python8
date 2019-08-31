import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic,QtGui,QtCore
from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QPushButton,QTableWidgetItem
from AnaDB import AnaDB

class TelApp(QWidget):
    #Telefon Menüsü PyQT
    def __init__(self,parent=None):
        super(TelApp, self).__init__(parent)
        self.telDialog = uic.loadUi(r"D:\ibrahim_ediz\Ornekler\GUI\TelefonDefteri\telEkleme.ui")
        self.veritabani = AnaDB()
        self.initUI()

    def initUI(self):
        self.telDialog.btKaydet.clicked.connect(self.telDialog.close)
    

    @pyqtSlot(int)
    def isimdegis(self,val=0):
        self.telDialog.txtTel.setText(str(val))
    def tetikleme(self,anaMenu=None):
        anaMenu.kayitId.connect(self.isimdegis)