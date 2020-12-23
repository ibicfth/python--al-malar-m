import sys ## komut satırından uygulamayı çalışırmk için argüman gönderebilmek için
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon  ## icon resmi
from PyQt5.QtWidgets import QToolTip ## araç tipi ismi

def window():
    app = QApplication(sys.argv) ##uygulama klasını çağırıp, 
    ## sys.argv  komut bilgisini uygulamaya aktardık.
    win = QMainWindow() #pencere oluşturduk
   
    win.setWindowTitle("pencere 1") ##pencere başlığı name
   
    win.setGeometry(200,500,500,800) #sol üst 0,0 dır. x=200 sağ,y=500 aşağı dan başla 
    ## 3.parametre pencere boyutu x=500, y=800 olsun
   
    win.setWindowIcon(QIcon('16_pyqt5/icone.jpg'))
   
    win.setToolTip('ilk aracım')

    win.show()
    ##pencereyi gösterdik ancak ne zaman kapanacağını aşağıda söyleriz
    sys.exit(app.exec_()) ##penceredeki çarpı ikonuna bastığımızda uygulma duracak.

window()


