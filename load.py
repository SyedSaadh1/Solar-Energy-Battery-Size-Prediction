# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'load.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(502, 222)
        MainWindow.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 160, 411, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(430, 20, 51, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 331, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(430, 50, 51, 33))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(430, 80, 51, 33))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(430, 110, 51, 33))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 311, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 80, 321, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 110, 391, 21))
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Load Profile Factors"))
        self.pushButton.setText(_translate("MainWindow", "Store Load Profile Factors in Data base"))
        self.lineEdit_4.setText(_translate("MainWindow", "0.90"))
        self.label_4.setText(_translate("MainWindow", "AverageLoad in KW(0.04 to 12.00)"))
        self.lineEdit_5.setText(_translate("MainWindow", "5.00"))
        self.lineEdit_6.setText(_translate("MainWindow", "1.00"))
        self.lineEdit_7.setText(_translate("MainWindow", "10"))
        self.label_6.setText(_translate("MainWindow", "PeakLoad in KW(0.50 to 40.00)"))
        self.label_7.setText(_translate("MainWindow", "MedianLoad in KW(0.02 to 12.00)"))
        self.label_8.setText(_translate("MainWindow", "Rated Photo Voltaic power in KW(3 to 25)"))


