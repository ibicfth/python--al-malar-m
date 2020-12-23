import sys
from PyQt5 import QtWidgets
from listview_from94file import Ui_MainWindow
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        ## load student hazır listeyi yükler
        self.loadStudent()

        ##kendimiz girmek için
        self.ui.btnAdd.clicked.connect(self.newAddStudent)

        ##edit ile öğrenci güncellemek için;
        self.ui.btnEdit.clicked.connect(self.editStudent)

        ##öğrenci silmek için;
        self.ui.btnRemove.clicked.connect(self.removeStudent)

        ## öğrenciyi yukarı satırlara taşımak için;
        self.ui.btnUp.clicked.connect(self.upStudent)

        ## öğrenciyi yukarı satırlara taşımak için;
        self.ui.btnDown.clicked.connect(self.downStudent)

        ##öğrenci listesini alfabetik sıralama yapmak için;
        self.ui.btnSort.clicked.connect(self.sortStudent)

        ## programı kapatmak için;
        self.ui.btnExit.clicked.connect(self.exitStudent)

    def loadStudent(self):
        self.ui.listItems.addItems(['ahmet','mehmet','veli'])
        self.ui.listItems.setCurrentRow(0)

    def newAddStudent(self):
        currentIndex=self.ui.listItems.currentRow()
        text, ok =QInputDialog.getText(self, 'new registration page','new registration student name')
        if text and ok is not None:
            self.ui.listItems.insertItem(currentIndex, text)

    def editStudent(self):
        index= self.ui.listItems.currentRow()
        list_eleman=self.ui.listItems.item(index) ## index numarasına göre item() methodu ile
        ## listItems dakielemanları alır.

        text, ok =QInputDialog.getText(self, 'öğrenci edit yap', 'değişiklik yap', QLineEdit.Normal, list_eleman.text())
        if text and ok is not None:
            list_eleman.setText(text)
    
    def removeStudent(self):
        index= self.ui.listItems.currentRow()
        list_eleman=self.ui.listItems.item(index) ## index numarasına göre item() methodu ile
        ## listItems dakielemanları alır.
        
        if list_eleman is None:
            return

        q=QMessageBox.question(self,'öğrenci sil',list_eleman.text()+ ' adlı öğrenciyi silmek istiyor musunuz?', QMessageBox.Yes | QMessageBox.No)
        if q==QMessageBox.Yes:
            sil_item=self.ui.listItems.takeItem(index)
            del sil_item

    def upStudent(self):
        index=self.ui.listItems.currentRow()
        if index >= 1:
            yukarı=self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index-1, yukarı)
            self.ui.listItems.setCurrentItem(yukarı) ## yukarı altığımız elemanın seçili olması ve tekrar yukaı bastığımızda yine aynı elemanın yukarı gitmesi için;

    def downStudent(self):
        index=self.ui.listItems.currentRow()
        if index <= self.ui.listItems.count()-1: ## seçtiğimiz elemanın en sonda olmadığını teyit ederiz
            asagi=self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index+1, asagi)
            self.ui.listItems.setCurrentItem(asagi) ## asağıya aldığımız elemanın seçili olması ve tekrar asağı bastığımızda yine aynı elemanın asağı gitmesi için;


    def sortStudent(self):
        self.ui.listItems.sortItems()

    def exitStudent(self):
        quit()
        
def app():
    app=QtWidgets.QApplication(sys.argv)
    win=myApp()
    win.show()
    sys.exit(app.exec_())

app()