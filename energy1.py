import sys
from energy import *
from PyQt5 import QtWidgets, QtGui, QtCore
import sqlite3
con = sqlite3.connect('battery1')


class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.insertvalues) 

   

  def insertvalues(self):
         
     with con:
    
        cur = con.cursor()
        aec = str(self.ui.lineEdit_4.text())
        ae = str(self.ui.lineEdit_5.text())
        heu = str(self.ui.lineEdit_6.text())
        hei = str(self.ui.lineEdit_7.text())
        ppd = str(self.ui.lineEdit_8.text())
        ppi = str(self.ui.lineEdit_9.text())		
        cur.execute('INSERT INTO energy VALUES(?,?,?,?,?,?)',(aec,ae,heu,hei,ppd,ppi))
        con.commit()
        
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())


