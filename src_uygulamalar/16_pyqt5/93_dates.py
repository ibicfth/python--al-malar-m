import sys
from PyQt5 import QtWidgets
from dates_from92file import Ui_MainWindow


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnCalculator.clicked.connect(self.calculator)

    def calculator(self):
        start=self.ui.dateStart.date()
        finish=self.ui.dateFinish.date()
        print(start, finish)

        ## ay içindeki gün sayısı
        print('verilen tarihteki ay {} gün çekiyor'.format(start.daysInMonth()))

        ## iki tarih arasındaki gün sayısını istersek
        print('aradaki gün sayısı {}'.format(start.daysTo(finish)))
def app():
    app=QtWidgets.QApplication(sys.argv)
    win=myApp()
    win.show()
    sys.exit(app.exec_())

app()