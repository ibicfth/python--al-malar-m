import sys
from PyQt5 import QtWidgets
from messagebox_from90file import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnExit.clicked.connect(self.showDialog)

    def showDialog(self):
        msg=QMessageBox()

        msg.setWindowTitle('Eminmisiniz')
        msg.setText('Silmek istediğinize eminmisiniz?')
        

        ## hazır butonlar eklemek için;
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Ignore | QMessageBox.Cancel)

        ## butonlardan herhangi biri varsayılan olması için,
        msg.setDefaultButton(QMessageBox.Cancel)

        ##buraya kadar olanları tek bir kodlada yapabiliriz. 
        # result=QMessageBox.question(self, 'eminmisiniz_2','silmek  istediğinize eminmisiniz_2', QMessageBox.Ok | QMessageBox.Ignore | QMessageBox.Cancel,QMessageBox.Cancel )
        # if result==QMessageBox.Ok:
        #     print('ok a bastınız_2')

        ##soru ikonu ekleyelim mesajın başına;
        msg.setIcon(QMessageBox.Question)

        ## detay butonu mesajı oluşturursak , butonu kendi oluşturur.
        msg.setDetailedText('eğer bu dosyayı silerseniz ...')

        ## dialog penceresinden herhangi bir butona tıkladığında işlem yapılması için;
        msg.buttonClicked.connect(self.popup_button)

        x=msg.exec_() ##bunu demezsek çalışmaz.

    def popup_button(self, i): ## ikinci paremetre i , hangi buton tıklanığını gösterir.
        print(i.text())

        ##buna göre if döngüleride oluşturabiliriz.
        if i.text() == 'OK':
            print('ok a bastınız...')
            QtWidgets.qApp.quit() ## formu kapatır ok a bastığımızda


def app():
    app=QtWidgets.QApplication(sys.argv)
    win=myApp()
    win.show()
    sys.exit(app.exec_())

app()