from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic

class miapp (QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("miapp.ui", self)
        self.BOTONCALC.clicked.connect(self.suma)

    
    def suma (self):
        resultado = int(self.NUMERO1.text()) + int(self.NUMERO2.text())
        self.ETRESULTADO.setText(str(resultado))

app = QApplication([])

win = miapp()
win.show()
app.exec()