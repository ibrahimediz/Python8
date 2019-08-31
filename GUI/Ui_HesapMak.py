# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\ibrahim_ediz\Ornekler\GUI\HesapMak.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(333, 301)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btdeneme = QtWidgets.QPushButton(self.centralwidget)
        self.btdeneme.setGeometry(QtCore.QRect(40, 40, 75, 23))
        self.btdeneme.setObjectName("btdeneme")
        self.btdeneme2 = QtWidgets.QPushButton(self.centralwidget)
        self.btdeneme2.setGeometry(QtCore.QRect(40, 80, 75, 23))
        self.btdeneme2.setObjectName("btdeneme2")
        self.txtAdi = QtWidgets.QLineEdit(self.centralwidget)
        self.txtAdi.setGeometry(QtCore.QRect(150, 40, 113, 20))
        self.txtAdi.setObjectName("txtAdi")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 333, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btdeneme.setText(_translate("MainWindow", "Düğmeli"))
        self.btdeneme2.setText(_translate("MainWindow", "Düğme 2"))

