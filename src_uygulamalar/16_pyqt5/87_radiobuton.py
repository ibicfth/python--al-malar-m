import sys
from PyQt5 import QtWidgets
from radiobutonfrom86file import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        ##----- setChecked()
        self.ui.radioTurkiye.setChecked(True) ## Türkiye varsayılan olarak seçili gelir.

        self.ui.radioLise.setChecked(True)

        ##----toggled() seçildiğinde yap anlamında;
        self.ui.radioTurkiye.toggled.connect(self.onClickedUlkeler)
        self.ui.radioAzerbaycan.toggled.connect(self.onClickedUlkeler)
        self.ui.radioKibris.toggled.connect(self.onClickedUlkeler)
        self.ui.radioFilistin.toggled.connect(self.onClickedUlkeler)
        self.ui.radioPakistan.toggled.connect(self.onClickedUlkeler)

        self.ui.radioIlkokul.toggled.connect(self.onClickedEgitim)
        self.ui.radioLise.toggled.connect(self.onClickedEgitim)
        self.ui.radioUniversite.toggled.connect(self.onClickedEgitim)
        self.ui.radioYuksekLisans.toggled.connect(self.onClickedEgitim)

        ## seçilenleri al butonuna tıklandığında;
        self.ui.btnUlkeler.clicked.connect(self.ulkeAl)
        self.ui.pushButton_2.clicked.connect(self.egitimAl)
      
      

    
    def onClickedUlkeler(self):
        rb=self.sender()
        if rb.isChecked():  ##eğer öge seçilmiş ise,tıklanmışşsa göstermesi için
            print('seçilen radio butonu: ' +rb.text())

    def onClickedEgitim(self):
        rb=self.sender()
        if rb.isChecked():  ##eğer öge seçilmiş ise,tıklanmışşsa göstermesi için
            print('seçilen radio butonu: ' +rb.text())

    def ulkeAl(self):
        #items1=self.ui.gridUlkeler.findChildren(QtWidgets.QRadioButton) ##ÇALIŞMAZ
        items2=self.ui.groupBoxUlkeler.findChildren(QtWidgets.QRadioButton) ##ÇALIŞIR
        ## items1 çalışmaz items2 çalışır çünkü birden çok farklı gruplama olduğu zaman
        ##örneğin dersler, meslekler vs gibi bunları kendi içindeki seçeneklerde işlem yapmak 
        ##istersek gridlayout vs ile bir hizaya bir bağlantı ilişkisi oluştursak bile 
        ## asıl ayrımı 2 çekilde yapıp grupları kendi arasında farklı işlmelere tabii tutabiliriz.
        ## ya grubları gridlayout ayırsak  bile ayrıca groupbox ın içine koyarız
        ##yada frame içine koymalıyız diğer türlü ayırma olmadan bütün elemanlar gelir (dersler+meslekler)


        for rb in items2: ## gelen bütün radiobutonları dolaş
            if rb.isChecked(): ## hangisi işaterli ise yani hangisi True ise
                self.ui.lblUlkeler.setText(rb.text())

    def egitimAl(self):
        items=self.ui.groupBoxEgitim.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lblEgitim.setText(rb.text())
def app():
    app=QtWidgets.QApplication(sys.argv)
    win=myApp()
    win.show()
    sys.exit(app.exec_())

app()

