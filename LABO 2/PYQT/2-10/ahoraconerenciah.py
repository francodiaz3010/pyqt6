from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mi ventana")
        label = QLabel("hola mundo") #crea etiquetas
        self.setCentralWidget(label)



app = QApplication([])

mi_ventana = MiVentana()
mi_ventana.show

app.exec()