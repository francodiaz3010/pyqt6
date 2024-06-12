import typing
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt6 import QtCore, uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("lineal.ui", self)
        self.boton.clicked.connect(self.boton_click)

    def boton_click(self):
        print(self.texto.text())

app = QApplication([])
win = MiVentana()
win.show()
app.exec()