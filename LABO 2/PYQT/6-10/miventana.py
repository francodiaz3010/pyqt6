from PyQt6.QtWidgets import QApplication, QMainWindow , QLabel
from PyQt6 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("miventana.ui", self)

app = QApplication([])
mi_ventana = MiVentana()
mi_ventana.show

app.exec()