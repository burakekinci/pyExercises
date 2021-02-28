import sys
from PyQt5 import QtWidgets
from UI_calc import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial

ERROR_MSG = "ERROR"

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp,self).__init__()
        self.setWindowTitle('Hesap Makinesi')
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connectSignals()

    #connecting button press signals and functions 
    def connectSignals(self):
        expressionButtons = {
            '0':self.ui.btn_0, '1':self.ui.btn_1, '2':self.ui.btn_2, '3':self.ui.btn_3, '4':self.ui.btn_4, '5':self.ui.btn_5, '6':self.ui.btn_6,
            '7':self.ui.btn_7, '8':self.ui.btn_8, '9':self.ui.btn_9, '+':self.ui.btn_add, '-':self.ui.btn_minus, '/':self.ui.btn_div,
            '*':self.ui.btn_multiply, '.':self.ui.btn_period,
        }

        self.ui.btn_enter.clicked.connect(self.evaluateExpression)
        self.ui.btn_clear.clicked.connect(self.clearExpression)

        for btnText,btn in expressionButtons.items():
            btn.clicked.connect(partial(self.buildExpression,btnText))

    #update or build result's string expression
    def buildExpression(self,sub_exp):
        expression = self.ui.txt_result.text() + sub_exp
        self.ui.txt_result.setText(expression)

    #clear the result area
    def clearExpression(self):
        self.ui.txt_result.setText('')

    #calculate the result's string expression with eval() function
    def evaluateExpression(self):
        expression = self.ui.txt_result.text()
        try:
            result = str(eval(expression))
        except Exception:
            result = ERROR_MSG
        self.ui.txt_result.setText(result)

def app():
    app = QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())

app()