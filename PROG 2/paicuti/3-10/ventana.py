import typing
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt6 import uic #Me permite relacionar el qt designer

class MiVentana (QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ventana.ui", self)

app = QApplication([])

win = MiVentana()
win.show()
print(win.label.text())
app.exec()