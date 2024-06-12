# 2. Vehículos:
#  - Clase Padre: 'Vehículo'
#  - Atributos:
#  - 'marca': La marca del vehículo.
#  - 'modelo': El modelo del vehículo.
#  - 'año': El año de fabricación del vehículo.
#  - Métodos:
#  - 'obtener_información()': Muestra la información completa del vehículo, incluyendo marca, modelo y
# año.
#  - Clase Hija: 'Automóvil'
#  - Atributos adicionales:
#  - 'tipo_carrocería': Tipo de carrocería del automóvil (sedán, SUV, etc.).
#  - 'cilindraje': La capacidad en cilindros del motor del automóvil.
#  - Métodos adicionales:
#  - 'calcular_impuesto()': Calcula el impuesto anual del automóvil basado en su cilindraje y año.
#  - Clase Hija: 'Motocicleta'
#  - Atributos adicionales:
#  - 'tipo_motor': Tipo de motor (2 tiempos, 4 tiempos, etc.).
#  - 'potencia': Potencia del motor en caballos de fuerza (HP).
#  - Métodos adicionales:
#  - 'calcular_seguro()': Calcula el costo anual del seguro de la motocicleta considerando su potencia y
# tipo de motor.
#  - Clase Hija: 'Camión'
#  - Atributos adicionales:
#  - 'carga_maxima': Capacidad máxima de carga del camión en kilogramos.
#  - Métodos adicionales:
#  - 'verificar_carga()': Verifica si la carga actual supera la carga máxima permitida y notifica al conductor.


class Vehiculo ():
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def __str__(self):
        return f"La marca del vehiculo es: {self.marca}, el modelo: {self.modelo}, y su año de fabricacion: {self.año}."
    
class Automovil (Vehiculo):
    def __init__(self, marca, modelo, año, carroceria, cilindraje):
        super().__init__(marca, modelo, año)
        self.carroceria = carroceria
        self.cilindraje = cilindraje
        self.impuesto = 0
    def calcimp (self):
        if self.cilindraje > 400:
            self.impuesto += 200
        elif self.cilindraje > 600:
            self.impuesto += 600
        elif self.cilindraje >800:
            self.impuesto += 1000
        if self.año < 2000:
            self.impuesto += 100
        elif self.año > 2000 and self.año <= 2010:
            self.impuesto += 400
        elif self.año > 2010 and self.año <= 2020:
            self.impuesto += 800
        elif self.año > 2020:
            self.impuesto += 1500
        return f"El impuesto anual es: {self.impuesto}"
    
class Motocicleta (Vehiculo):
    def __init__(self, marca, modelo, año, tipomot, potencia): 
        super().__init__(marca, modelo, año)
        self.tipomot = tipomot #2T o 4T
        self.potencia = potencia
        self.seguro = 0
    def calcseg (self):
        if self.tipomot == 2:
            self.seguro += 500
        else:
            self.seguro += 1500
        if self.potencia > 100:
            self. seguro += 1500
        else:
            self.seguro += 500
        return f"El seguro anual es: {self.seguro}" 

class Camion (Vehiculo):
    def __init__(self, marca, modelo, año, cargamax):
        super().__init__(marca, modelo, año)
        self.cargamax = cargamax
    def verif (self, carga):
        if carga > self.cargamax:
            return "La carga actual eccede la carga maxima permitida del vehiculo."
        else:
            return "Carga permitida."

auto1 = Automovil("Honda", "Fit", 2013, "sedan", 500)
print(auto1.calcimp())
moto1 = Motocicleta("Honda", "XR", 2018, 4, 400)
print(moto1)
print(moto1.calcseg()) 
camion1 = Camion ("Mercedes Benz", "Scania", 2020, 5000)
print(camion1.verif(5000000))
print(camion1)