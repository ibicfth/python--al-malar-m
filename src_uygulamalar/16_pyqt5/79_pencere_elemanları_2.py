### 77.ci ve 78.ci dersteki fonksiyon içinde tanımladığımızı burda klass sınıf içinde yapacağız

import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon 
from PyQt5.QtWidgets import QToolTip 

class MyWindow(QMainWindow): ##mywindow sınıfı QMainWindow tan türetilsin onun özelliklerini taşısın
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setWindowTitle("pencere 1") 
    
        self.setGeometry(200,500,500,800) 
    
        self.setWindowIcon(QIcon('16_pyqt5/icone.jpg'))
    
        self.setToolTip('ilk aracım')

        self.pencereElemanlari()

    def pencereElemanlari(self):
         
        self.lbl_name= QtWidgets.QLabel(self) 
        self.lbl_name.setText('adiniz: ') 
        self.lbl_name.move(50,30) 

        self.lbl_surname=QtWidgets.QLabel(self)
        self.lbl_surname.setText('soyadiniz: ')
        self.lbl_surname.move(50,80)
        
        self.lbl_result=QtWidgets.QLabel(self)
        self.lbl_result.move(150,150)
        self.lbl_result.resize(200,32)

        self.text_name= QtWidgets.QLineEdit(self)
        self.text_name.move(150,30)
        self.text_name.resize(200,22) ##textbox kutusunun boyutunu ayarlar

        self.text_surname= QtWidgets.QLineEdit(self)
        self.text_surname.move(150,80)
        self.text_surname.resize(200,22) ##textbox kutusunun boyutunu ayarlar

        self.save_button=QtWidgets.QPushButton(self)
        self.save_button.setText('Kaydet')
        self.save_button.move(150,120)
        self.save_button.clicked.connect(self.click_yap) 
    
    def click_yap(self):
        self.lbl_result.setText(self.text_name.text() + '  ' +self.text_surname.text() +' kaydı eklendi.')
        

def window():
    app = QApplication(sys.argv) 
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()