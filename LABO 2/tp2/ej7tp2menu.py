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
peaje1 = Peaje("El zonda", "San blas")
print ("---MENU---^^\na)Ingresar vehiculo\nb)Calcular total peaje\nc)Cantidad de vehiculos\nd)Salir")
menu = 0
while menu != "d":
    menu = input("ingrese la opcion: ")
    if menu == "a":
        print("Por favor elija el tipo de vehiculo a ingresar: \na)Auto\nb)Moto\nc)Camion ")
        vehicul = input("ingrese la opcion correspondiente: ")
        if vehicul == "a":
            placa = input("ingrese la placa del auto: ")
            peaje1.agregar_vehiculos(Auto(placa))
            print("Vehiculo agregado")
        elif vehicul == "b":
            placa = input("ingrese la placa de la moto: ")
            peaje1.agregar_vehiculos(Moto(placa))
            print("Vehiculo agregado")
        elif vehicul == "c":
            placa = input("ingrese la placa del camion: ")
            ejes = int(input("ingrese la cantidad de ejes: "))
            peaje1.agregar_vehiculos(Camion(placa, ejes))
            print("Vehiculo agregado")
    elif menu == "b":
        print("El total es: ", peaje1.calcular_total_peaje())
    elif menu == "c":
        print("La cantidad de vehiculos fueron: ", peaje1.cantidad_vehiculos())
    elif menu == "d":
        print("Hasta luego.")