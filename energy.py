# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'energy.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(779, 271)
        MainWindow.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 210, 411, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(570, 20, 61, 33))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 481, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(570, 50, 61, 33))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(570, 80, 61, 33))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(570, 110, 61, 33))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 431, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 80, 521, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 110, 531, 21))
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 140, 491, 21))
        self.label_10.setObjectName("label_10")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(570, 140, 61, 33))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(570, 170, 61, 33))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 170, 501, 21))
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Energy Profile Factors"))
        self.pushButton.setText(_translate("MainWindow", "Store Energy Profile Factors in Data base"))
        self.lineEdit_4.setText(_translate("MainWindow", "5000"))
        self.label_4.setText(_translate("MainWindow", "Annual Energy Consumption in KWH(620 to 100000)"))
        self.lineEdit_5.setText(_translate("MainWindow", "10000"))
        self.lineEdit_6.setText(_translate("MainWindow", "5000"))
        self.lineEdit_7.setText(_translate("MainWindow", "2000"))
        self.label_6.setText(_translate("MainWindow", "Accumualted Energy in KWH(100 to 80000)"))
        self.label_7.setText(_translate("MainWindow", "No.of Hours of Energy Utilization From Grid(4000 to 8000)"))
        self.label_8.setText(_translate("MainWindow", "No.of Hours of Energy Injection into the Grid(1000 to 3000)"))
        self.label_10.setText(_translate("MainWindow", "Peak power drawn from the grid in KW( 1.00 to 40.00)"))
        self.lineEdit_8.setText(_translate("MainWindow", "5.00"))
        self.lineEdit_9.setText(_translate("MainWindow", "10.00"))
        self.label_11.setText(_translate("MainWindow", "Peak power injected into the grid in KW(3.00 to 20.00)"))


