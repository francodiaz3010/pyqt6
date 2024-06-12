class Vehiculo():
    def __init__(self, placa):
        self.placa = placa

class Moto(Vehiculo):
    def __init__(self, placa):
        super().__init__(placa)
        self.valor_peaje = 150

class Auto(Vehiculo):
    def __init__(self, placa):
        super().__init__(placa)
        self.valor_peaje = 300
    
class Camion (Vehiculo):
    def __init__(self, placa, cantidad_ejes):
        super().__init__(placa)
        self.cantidad_ejes = cantidad_ejes
        self.valor_peaje = 500 * self.cantidad_ejes

class Peaje():
    def __init__(self, nombre, departamento):
        self.nombre = nombre
        self.departamento = departamento
        self.vehiculoss = []
    def agregar_vehiculos (self, vehic):
        self.vehiculoss.append(vehic)
    def calcular_total_peaje(self):
        acc = 0
        for vehi in self.vehiculoss:
            acc += vehi.valor_peaje
        return acc
    def cantidad_vehiculos(self):
        return len(self.vehiculoss)
    
peaje1 = Peaje("El zonda", "Aimogasta")
moto1 = Moto("asd")
auto1 = Auto("qwe")
camion1 = Camion("uio", 4)
peaje1.agregar_vehiculos(moto1)
peaje1.agregar_vehiculos(auto1)
peaje1.agregar_vehiculos(camion1)
print(peaje1.calcular_total_peaje())
print(peaje1.cantidad_vehiculos())