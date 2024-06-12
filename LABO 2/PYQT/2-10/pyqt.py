from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel


app = QApplication([])

window = QMainWindow() #crea ventana
window.setWindowTitle("Mi ventana")#titulo


label = QLabel("hola mundo") #crea
window.setCentralWidget(label)
window.show()#muestra
app.exec() #Ejecuta