import sys
from PyQt5 import QtWidgets
from UI_calc import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp,self).__init__()
        self.setWindowTitle('Hesap Makinesi')
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
def app():
    app = QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())

app()