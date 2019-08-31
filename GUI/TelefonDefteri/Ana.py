import sys
from PyQt5.QtCore import pyqtSlot,pyqtSignal
from PyQt5 import uic,QtGui,QtCore
from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit,QPushButton,QTableWidgetItem
from AnaDB import AnaDB
from Ekleme import TelApp
class App(QMainWindow):
    kayitId = pyqtSignal(int)
    #Telefon Defteri PyQT
    def __init__(self):
        super().__init__()
        self.pencere = uic.loadUi(r"D:\ibrahim_ediz\Ornekler\GUI\TelefonDefteri\Ana.ui")
        self.veritabani = AnaDB()
        self.pencere.tblListe.setHorizontalHeaderLabels(["ID","ADI","SOYADI","ILI","ILCESI"])
        self.initUI()
        
    def initUI(self):
        self.tabloDoldur()
        self.comboIlDoldur()
        self.pencere.TelEkleme.triggered.connect(self.tiklandi)
        self.pencere.show()
    
    def setPencere(self,nesne):
        self.telApp = TelApp(self)
        self.telApp.tetikleme(nesne)

    def tabloDoldur(self):
        liste = self.veritabani.kisiListele()
        self.pencere.tblListe.doubleClicked.connect(self.tabloSecim)
        self.pencere.tblListe.setRowCount(10)
        self.pencere.tblListe.setColumnCount(len(liste[0]))
        for i in range(0,len(liste)):
            for j in range(0,len(liste[0])):
                self.pencere.tblListe.setItem(i,j,QTableWidgetItem(str(liste[i][j])))

    def tabloSecim(self):
        for currentQTableWidgetItem in self.pencere.tblListe.selectedItems():
            satir = currentQTableWidgetItem.row()
            self.pencere.lblID.setText(self.pencere.tblListe.item(satir,0).text())
            self.pencere.txtAdi.setText(self.pencere.tblListe.item(satir,1).text())
            self.pencere.txtSoyadi.setText(self.pencere.tblListe.item(satir,2).text())
            self.pencere.cmbIl.setCurrentText(self.pencere.tblListe.item(satir,3).text())
            self.pencere.cmbIlce.setCurrentText(self.pencere.tblListe.item(satir,4).text())
            self.kayitId.emit(int((self.pencere.tblListe.item(satir,0).text())))
    
    def tiklandi(self):
        self.telApp.telDialog.show()

    def comboIlDoldur(self):
        self.pencere.cmbIl.addItem("Seçiniz",-1)
        liste = self.veritabani.ilListele()
        for a,b in liste:
            self.pencere.cmbIl.addItem(b,a)
        self.pencere.cmbIl.currentIndexChanged.connect(self.comboSecim)

    def comboIlceDoldur(self,ilID):
        liste = self.veritabani.ilceListe(ilID)
        self.pencere.cmbIlce.clear()
        self.pencere.cmbIlce.addItem("Seçiniz",-1)
        for a,b in liste:
            self.pencere.cmbIlce.addItem(b,a)


    def comboSecim(self,i):
        sonuc = self.pencere.cmbIl.itemData(i)
        self.comboIlceDoldur(sonuc)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.setPencere(ex)
    sys.exit(app.exec_())