import sys
from PyQt5 import QtWidgets
from combobox_from88file import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.comboBox.addItem('ankara') ##yada

        combo=self.ui.comboBox
        combo.addItem('mersin')
        combo.addItem('manisa')

        ##çoklu eklemek için;
        ##combo.addItems(['kars','kayseri','ordu','rize'])

        ##ekleme işlemini sınıfa ekleyebiliriz.
        self.ui.btnGetItem.clicked.connect(self.getItems)

        ##ekli olan elemanın bilgilerini getirmek için
        self.ui.btnLoadItem.clicked.connect(self.loadItems)
    
    def loadItems(self):
        sehirler=['kars','kayseri','ordu','rize']
        self.ui.comboBox.addItems(sehirler)

    def getItems(self):
        print(self.ui.comboBox.currentText())

        ## yada index e göre hepsini getirmek için count sınıfını kullanabiliriz.
        ## kaç eleman olmadığı durumlarda count kaç eleman olduğunu hesaplar;
        ##itemtext ilede index e göre elemanları yazırırız.
        count=self.ui.comboBox.count()
        for index in range(count):
            print(self.ui.comboBox.itemText(index))


def app():
    app=QtWidgets.QApplication(sys.argv)
    win=myApp()
    win.show()
    sys.exit(app.exec_())

app()

