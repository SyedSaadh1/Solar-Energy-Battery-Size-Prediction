import sys
import os
from battery import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton_3.clicked.connect(self.lpf)
     self.ui.pushButton.clicked.connect(self.epf)
     self.ui.pushButton_2.clicked.connect(self.crcsv)
     self.ui.pushButton_5.clicked.connect(self.gnb)
     self.ui.pushButton_6.clicked.connect(self.bnb)

  def lpf(self):
    os.system("python load1.py")
	
  def epf(self):
    os.system("python energy1.py")

  def crcsv(self):
    os.system("python createcsv1.py")
	
  def gnb(self):
    os.system("python gnb1.py")

  def bnb(self):
    os.system("python bnb1.py")
   
if __name__ == "__main__":  
    try:
        app = QtWidgets.QApplication(sys.argv)
        myapp = MyForm()
        myapp.show()
        sys.exit(app.exec_())
    except:
        pass
