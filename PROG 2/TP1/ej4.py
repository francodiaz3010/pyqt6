#Modela una clase Coche que represente un vehículo. Define los atributos necesarios para
#almacenar la marca, modelo, año y velocidad actual del coche. Implementa métodos para
#acelerar y frenar el coche, actualizando su velocidad en función de los valores proporcionados.

class Coche():
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.veloc = 0
    
    def acelerar (self,vel):
        self.veloc += vel
    def frenar (self, vel):
        self.veloc -= vel
    
coche1 = Coche("Honda", "civic", 2000)
coche1.acelerar(50)
coche1.frenar(20)
coche1.acelerar(100)
print(coche1.veloc)