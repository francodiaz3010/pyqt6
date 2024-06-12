from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6 import uic

class MiVentana (QMainWindow):
    def __init__ (self):
        uic.load_ui()
        self.mensaje.clicked.connect(self.on_mensaje)

    def on_mensaje(self):
        msg = QMessageBox()
        msg.setWindowTitle("Titulo del mensaje")
        msg.setText("Este es un mensaje")
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel)

        respuesta = msg.exec ()

app = QApplication([])

win = MiVentana()
win.show()

app.exec()