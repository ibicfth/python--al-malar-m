### HESAP MAKİNASI

import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFont  ## font size ayarlamak için

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()

        self.setWindowTitle("hesap yapma")
        self.setGeometry(100,100,500,500)
        self.pencereElemanlari()

        

    def pencereElemanlari(self):

        self.sayi_1=QtWidgets.QLabel(self)
        self.sayi_1.setText("sayi 1: ")
        self.sayi_1.move(50,30)
        self.sayi_1.setFont(QFont('Arial', 12)) 

        self.sayi_1_box = QtWidgets.QLineEdit(self)
        self.sayi_1_box.move(110,35)
        self.sayi_1_box.resize(100,20)

        self.sayi_2=QtWidgets.QLabel(self)
        self.sayi_2.setText("sayi 2: ")
        self.sayi_2.move(50,70)
        self.sayi_2.setFont(QFont('Arial', 12)) 

        self.sayi_2_box = QtWidgets.QLineEdit(self)
        self.sayi_2_box.move(110,75)
        self.sayi_2_box.resize(100,20)

        self.btn_toplama = QtWidgets.QPushButton(self)
        self.btn_toplama.move(110,110)
        self.btn_toplama.setText("toplama")
        self.btn_toplama.clicked.connect(self.islemSec)

        self.btn_cikarma = QtWidgets.QPushButton(self)
        self.btn_cikarma.move(110,150)
        self.btn_cikarma.setText("çıkarma")
        self.btn_cikarma.clicked.connect(self.islemSec)

        self.btn_carpma = QtWidgets.QPushButton(self)
        self.btn_carpma.move(110,190)
        self.btn_carpma.setText("çarpma")
        self.btn_carpma.clicked.connect(self.islemSec)

        self.btn_bölme = QtWidgets.QPushButton(self)
        self.btn_bölme.move(110,230)
        self.btn_bölme.setText("bölme")
        self.btn_bölme.clicked.connect(self.islemSec)

        self.result = QtWidgets.QLabel(self)
        self.result.move(110,270)
        self.result.setText('sonuc')

    def islemSec(self):
        islem=self.sender()
        if islem.text() == 'toplama':
            sonuc=int(self.sayi_1_box.text()) + int(self.sayi_2_box.text())
            

        elif islem.text() == 'çıkarma':
            sonuc=int(self.sayi_1_box.text()) - int(self.sayi_2_box.text())
            

        elif islem.text() == 'çarpma':
            sonuc=int(self.sayi_1_box.text()) * int(self.sayi_2_box.text())
            

        elif islem.text() == 'bölme':
            sonuc=int(self.sayi_1_box.text()) / int(self.sayi_2_box.text())
            
        self.result.setText('sonuc: '+ str(sonuc))

def window():
    app=QApplication(sys.argv)
    win=MyWindow()
    win.show()
    sys.exit(app.exec_())

window()