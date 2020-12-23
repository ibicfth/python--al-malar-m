import sys
from PyQt5 import QtWidgets
from tableview_from96file import Ui_MainWindow
from PyQt5.QtWidgets import QTableWidgetItem

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadProducts()
        self.ui.btnSave.clicked.connect(self.addProduct)

    def addProduct(self):
        name=self.ui.lineName.text() ## grilen name
        price=self.ui.linePrice.text() ## grilen fiyatı aldık

        eleman=self.ui.tblProducts.rowCount() ## zaten olan eleman sayısı,eleman sayısı 1 den başlar
        ##şimdide yeni ekleyeceğimiz satırı oluşturalım.
        self.ui.tblProducts.insertRow(eleman) #insert 0 dan başlar yani eleman sayısı 4 gelirse aslında 5. satırı eklemiş oluruz.
        
        self.ui.tblProducts.setItem(eleman,0,QTableWidgetItem(name))
        self.ui.tblProducts.setItem(eleman,1,QTableWidgetItem(price))

    def loadProducts(self):
        ## YOL : 1 MANUAL
        '''
        ## tableWidget ın satır sutun sayısını belirtmek için;
        self.ui.tblProducts.setRowCount(3) ## üç satır (üç ürünlü)
        self.ui.tblProducts.setColumnCount(2) ## her ürünün iki sutunu var isim ve fiyat gibi,
         
        ##oluşturduğumuz satır ve sutun başlığı verebiliriz.
        self.ui.tblProducts.setHorizontalHeaderLabels(('Name','Price')) ##yatay (sütün başlıkları)
        #self.ui.tblProducts.setVerticalHeaderLabels() ## satırlara isim vermek istersekte bu şekilde

        ##colon genişlik ayarı
        self.ui.tblProducts.setColumnWidth(0,200)
        self.ui.tblProducts.setColumnWidth(1,50)

        ##ürün eklemek için;
        self.ui.tblProducts.setItem(0,0,QTableWidgetItem('samsung s8'))
        self.ui.tblProducts.setItem(0,1,QTableWidgetItem('4500'))

        self.ui.tblProducts.setItem(1,0,QTableWidgetItem('nokia'))
        self.ui.tblProducts.setItem(1,1,QTableWidgetItem('3500'))

        self.ui.tblProducts.setItem(2,0,QTableWidgetItem('iphone'))
        self.ui.tblProducts.setItem(2,1,QTableWidgetItem('8000'))
        '''

        ## YOL : 2 DİNAMİK 

        ##----yukarıda satır sütünu kendimiz belirledik, ancak sayısını bilmediğimiz kadar ürün oldugunda
        ##----yada serverdan gelen ürünler olduğunda dinamik olarak tableview eklemek için;
        ##örneğin serverda  products diye bir tablo olsun ve bu tablodan name ve fiyatlar olsun
        ##biz server baglantı kurmak yerine aşağıda serverdn tabloyu ulaşıp almış gibi ekleyelim ve
        ##programa dinamik olarak verelim

        products=[
            {'name':'samsung s6','price':2200},
            {'name':'samsung s7','price':3200},
            {'name':'samsung s8','price':4200},
            {'name':'samsung s9','price':5200},
            {'name':'iphone 7','price':6200},
            {'name':'iphone 7s','price':6500},
            {'name':'iphone 8','price':7200},
            {'name':'iphone 8s','price':7800},
            {'name':'iphone 9','price':8200},
            {'name':'iphone 9s','price':8800}
        ]
        self.ui.tblProducts.setRowCount(len(products)) ## satır kaç ürün geleceği dinamik
        self.ui.tblProducts.setColumnCount(2) ## kolon kısmı dinamik değil 

        self.ui.tblProducts.setHorizontalHeaderLabels(('Name','Price'))

        #buraya kadar tabloyu veri sayısına kadar oluşturduk şimdi tabloyu dolduralım

        urunSatırNo=0
        for urunler in products:

            self.ui.tblProducts.setItem(urunSatırNo,0,QTableWidgetItem(urunler['name']))
            self.ui.tblProducts.setItem(urunSatırNo,1,QTableWidgetItem(str(urunler['price'])))

            urunSatırNo += 1



def app():
    app=QtWidgets.QApplication(sys.argv)
    win=myApp()
    win.show()
    sys.exit(app.exec_())

app()