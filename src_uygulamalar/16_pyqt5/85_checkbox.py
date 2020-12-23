import sys
from PyQt5 import QtWidgets
from checkbox_from84file import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        ##--- cbSinema checkbox ının stateChanged özelliği ile tıklama durumuna göre showstate sınıfında yapmasını istdiğimiz şeyi tanımlarız.
        self.ui.cbSinema.stateChanged.connect(self.showState)

        self.ui.cbKitapOkumak.stateChanged.connect(self.showState)
        self.ui.cbSpor.stateChanged.connect(self.showState)

        self.ui.pushButton.clicked.connect(self.getAllHobiler)
        self.ui.pushButton_2.clicked.connect(self.getAllDersler)

    def showState(self, value): ## o an kiseçim değeri ne ise onu getirir.statechanged den gelir.
        ## tıklı ise 2 , değilse 0 üretir.
        
        # print (value)
        # print (self.ui.cbSinema.isChecked()) ##checkboz seçili ise true değilse false döndürür.
        # print (self.ui.cbSinema.text()) ## checkbox un testini getirir.
        
        # print (self.ui.cbKitapOkuma.isChecked()) ##checkboz seçili ise true değilse false döndürür.
        # print (self.ui.cbKitapOkuma.text()) 

        # print (self.ui.cbSpor.isChecked()) ##checkboz seçili ise true değilse false döndürür.
        # print (self.ui.cbSpor.text()) 

        ## yukardakileri her checkbox için yapacağımıza sender ile hangi butonu tıkladıysak onu algılayıp 
        ## ona göre işlem yapar. yani hangisi seçilirse onun bilgilerini getirir. Sender()

        cb=self.sender()
        print(value)
        print(cb.text())
        print(cb.isChecked())

    def getAllHobiler(self):
        #items=self.ui.centralwidget.findChildren(QtWidgets.QCheckBox) ##şuan formdaki bütüncheckboxlar liste elemanı halinde gelir.
        items=self.ui.groupHobiler.findChildren(QtWidgets.QCheckBox) ## sadece grouphobilerdeki checkbox ları alır.
        ## istediklerimizin ve tek tek gelmesini istiyorsak;
        result=''
        for cb in items:
            
            if cb.isChecked():
                result += cb.text() + '\n' 
                
        self.ui.lblResultHobiler.setText(result)
        
    def getAllDersler(self):
        #items=self.ui.centralwidget.findChildren(QtWidgets.QCheckBox) ##şuan formdaki bütüncheckboxlar liste elemanı halinde gelir.
        items=self.ui.groupDersler.findChildren(QtWidgets.QCheckBox) ## sadece grouphobilerdeki checkbox ları alır.
        ## istediklerimizin ve tek tek gelmesini istiyorsak;
        
        result=''
        for cb in items:
            
            if cb.isChecked():
                result += cb.text() + '\n' 
                    
        self.ui.lblResultDersler.setText(result)
                


def app():
    app=QtWidgets.QApplication(sys.argv)
    win=myApp()
    win.show()
    sys.exit(app.exec_())

app()

