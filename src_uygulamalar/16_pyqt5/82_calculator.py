from PyQt5 import QtWidgets
import sys
from designer_Calculator_from81file import Ui_MainWindow_1 ## designer_Calculator_81.py dan Ui_mainwindow classını import

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp,self).__init__()
        self.ulas=Ui_MainWindow_1()
        self.ulas.setupUi(self) ## ui_mainwindow_1 classının setupUi sınıfını çağırır.

        ##buraya kadar tasarım kısmını designerdan aldık tıklama sonrasının ne yapacağını yazalım.
        self.ulas.btn_toplama.clicked.connect(self.islemSec)
        self.ulas.btn_cikarma.clicked.connect(self.islemSec)
        self.ulas.btn_carpma.clicked.connect(self.islemSec)
        self.ulas.btn_bolme.clicked.connect(self.islemSec)

    def islemSec(self):
        islem=self.sender()
        if islem.text() == 'toplama':
            sonuc=int(self.ulas.sayi_1_box.text()) + int(self.ulas.sayi_2_box.text())
            

        elif islem.text() == 'çıkarma':
            sonuc=int(self.ulas.sayi_1_box.text()) - int(self.ulas.sayi_2_box.text())
           

        elif islem.text() == 'çarpma':
            sonuc=int(self.ulas.sayi_1_box.text()) * int(self.ulas.sayi_2_box.text())
            
        elif islem.text() == 'bölme':
            sonuc=int(self.ulas.sayi_1_box.text()) / int(self.ulas.sayi_2_box.text())
            
        self.ulas.lbl_sonuc.setText('sonuc: '+ str(sonuc))

def app():
    app=QtWidgets.QApplication(sys.argv)
    win=MyApp()
    win.show()
    sys.exit(app.exec_())

app()

