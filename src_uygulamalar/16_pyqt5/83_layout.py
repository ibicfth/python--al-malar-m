import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPalette, QColor

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100,100,500,500)
        
        # ## ------  BOX LAYOUT OLUŞTURMA İLE BOYAMA -------

        # ##----------- widget ekleme ,  3 tane dikey widget ekledik
        # # layout=QtWidgets.QVBoxLayout()
        # # layout.addWidget(Color('yellow'))
        # # layout.addWidget(Color('red'))
        # # layout.addWidget(Color('black'))

        # ## şimdi iki tane yatay widget ı bir dikey widget da ekleyelim,
        # hlayout1=QtWidgets.QHBoxLayout()
        # hlayout1.addWidget(Color('white'))
        # hlayout1.addWidget(Color('black'))
        # hlayout1.addWidget(Color('white'))
        
        # hlayout1.setContentsMargins(50,0,10,20) #hlayout1 in 4 köşesinden boşluk bıraktırır.
        # yada köşelerden değilde hlayout1 in widgetları arasında boşluk oluşturmak için;
        # hlayout1.setSpacing(50) 

        
        # hlayout2=QtWidgets.QHBoxLayout()
        # hlayout2.addWidget(Color('red'))
        # hlayout2.addWidget(Color('yellow'))

        # vlayout=QtWidgets.QVBoxLayout()
        # vlayout.addLayout(hlayout1)
        # vlayout.addLayout(hlayout2) ## vlayout a widget eklemedik yukrda oluşturdupumuz hlayout 1 ve 2 yi ekledik.

        # widget=QWidget()
        # widget.setLayout(vlayout)
        ## -------------------------------------------

        ## GRİD LAYOUT OLUŞTURMA İLE BOYAMA
        ##grid layout ta index e göre boyama yapabiliriz.
        layout = QtWidgets.QGridLayout()
        layout.addWidget(Color('black'),0,0)
        layout.addWidget(Color('blue'),1,0)
        layout.addWidget(Color('orange'),1,3)
        layout.addWidget(Color('green'),2,2)
        layout.addWidget(Color('yellow'),3,1)

        widget=QWidget()
        widget.setLayout(layout)
        #widget = Color('black')  # tekbir widget tanımladık box yada grid layout oluşturmadan formun hepsini boyadık
        self.setCentralWidget(widget)

def app():
    app= QApplication(sys.argv)
    win=MainWindow()
    win.show()
    sys.exit(app.exec_())

app()