class Motor ():
    def __init__(self, aceite, temp):
        self.aceite = aceite
        self.temp = temp
        self.encendido = False
        
    def arrancar(self):
        if self.encendido == False:
            self.encendido = not self.encendido
            return f"Motor encendido."
        else:
            f"Motor ya encendido, no se puede sobreencender."
    def detener(self):
        if self.encendido == True:
            self.encendido = not self.encendido
            return f"Motor apagado."
        else:
            return f"Motor ya apagado."
    def __str__(self):
        return f"El nivel de aceite es: {self.aceite}, la temperatura es: {self.temp}. Esta encendido?: {self.encendido}."
    


class Rueda ():
    def __init__(self, rodado, presion):
        self.rodado = rodado
        self.presion = presion
    def inflar (self, agregar):
        self.presion += agregar
    def desinflar (self, quitar):
        self.presion -= quitar
    def __str__(self):
        return f"El rodado de la rueda es: {self.rodado} y la presion de la misma es: {self.presion}"
    
class Ventana ():
    def __init__(self, polarizado):
        self.polarizado = polarizado
        self.abierto = False
    def abrir (self):
        self.abierto = True
    def cerrar (self):
        self.abierto = False
    def __str__(self):
        return f"La venta esta polarizada?: {self.polarizado}, esta abierta?: {self.abierto}"
class Puerta ():
    def __init__(self, ventana, color):
        self.ventana = ventana
        self.color = color
        self.abierto = False
    def abrir (self):
        self.abierto = True
    def cerrar (self):
        self.abierto = False
    def __str__(self):
        return f"la puerta tiene una ventana cons los siguientes atributos: {self.ventana}, la puerta es de color: {self.color}. La puerta, esta abierta ? {self.abierto}"
        
class Auto ():
    def __init__(self, motor, rueda1, rueda2, rueda3, rueda4, puerta1, puerta2):
        self.motor = motor
        self.rueda1 = rueda1
        self.rueda2 = rueda2
        self.rueda3 = rueda3
        self.rueda4 = rueda4
        self.puerta1 = puerta1
        self.puerta2 = puerta2
    def __str__(self):
        return f"Auto: Los atributos del motor son: {self.motor}, las puertas: {self.puerta1}, {self.puerta2} y las ruedas: {self.rueda1}, {self.rueda2}, {self.rueda3}, {self.rueda4}."



motor1 = Motor(4.5, 30)
motor1.arrancar()
#print(motor1)

rueda1 = Rueda(14, 150)
rueda2 = Rueda(20, 200)
#print(rueda1, rueda2)

ventana1 = Ventana(True)
#print(ventana1)

puerta1 = Puerta(ventana1, "roja")
puerta2 = Puerta(ventana1, "Azul")
#print(puerta1, puerta2)

auto1 = Auto(motor1, rueda1, rueda1, rueda2, rueda2, puerta1, puerta2)
print(auto1.rueda1)
print(auto1.rueda2)
#print(auto1)
auto1.rueda1.rodado = 16
print(auto1.rueda1)
print(auto1.rueda2)