import typing
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox |
from PyQt6 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("combobox.ui", self)
        self.comboBox.currentTextChanged.connect(self.onChange)
        self.removebtn.clicked.connect(self.onRemove)
        self.addbtn.clicked.connect(self.onAdd)
    
    def onChange(self):
        print(self.comboBox.currentText())
        print(self.comboBox.currentIndex())
    
    def onRemove (self):
        msg = QMessageBox
        msg.setWindowTitle ("Advertencia")
        msg.setText("Esta seguro que desea eliminar ese elemento? ")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        respuesta = msg.exec()

        if respuesta == QMessageBox.StandardButton.Yes:
            index = self.comboBox.currentIndex()
            self.comboBox.removeItem(index)

    def onAdd (self):
        text = self.addtext.text()
        self.comboBox.addItem(text)

app = QApplication([])
win = MiVentana()
# print(win.etiqueta.text())
# win.etiqueta.setText("Hola mundo") #Cambio el atributo con el metodo setText
win.show()
app.exec()