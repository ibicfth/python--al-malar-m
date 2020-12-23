from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys




def window():
    app = QApplication(sys.argv) ##uygulama klasını çağırıp, 
    ## sys.argv  komut bilgisini uygulamaya aktardık.
    win = QMainWindow() #pencere oluşturduk

    ##---- label ekleme;
    lbl_name= QtWidgets.QLabel(win) # win pencresine label elemanı ekledik
    lbl_name.setText('adiniz: ') ##eklediğimiz elemanın adını belirledik

    lbl_name.move(50,30) ##lbl_name i hareket ettirmek konmlamak,

    lbl_surname=QtWidgets.QLabel(win)
    lbl_surname.setText('soyadiniz: ')
    lbl_surname.move(50,80)


    ##---- lineEdit ekleme;
    text_name= QtWidgets.QLineEdit(win)
    text_name.move(150,30)

    text_surname= QtWidgets.QLineEdit(win)
    text_surname.move(150,80)

    def click_yap(self):
        print('database e adı: ' + text_name.text() +' ve soyadı: ' + text_surname.text()+ ' olan kullanıcı eklendi.' )
    
    ##------ pushbuton ekleme;
    save_button=QtWidgets.QPushButton(win)
    save_button.setText('Kaydet')
    save_button.move(150,120)

    ##butona tıklandığında bunu algılayan ve sonrasında başka bir eylemi başlatmak içinse;
    save_button.clicked.connect(click_yap) 
    ##save_buttonuna clicked connect özelliğini ekleyip bu özellik çağrıldığında click_yap die tanımladığımız fonksiyonu çağırır.
    
    
    win.show()
    sys.exit(app.exec_())

window()