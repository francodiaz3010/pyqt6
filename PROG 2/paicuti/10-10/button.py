import typing
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt6 import QtCore, uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("button.ui", self)
        self.boton.clicked.connect(self.on_clicked)
    
    def on_clicked(self):
        if self.etiqueta.text() == "Hola mundo":
            self.etiqueta.setText("Chau mundo")
        else:
            self.etiqueta.setText("Hola mundo")
app = QApplication([])
win = MiVentana()
print(win.etiqueta.text())
# win.etiqueta.setText("Hola mundo") #Cambio el atributo con el metodo setText
win.show()
app.exec()