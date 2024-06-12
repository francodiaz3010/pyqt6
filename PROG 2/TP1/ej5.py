# Crea una clase Banco que simule un banco. Define atributos para el nombre del banco, el saldo
# total, las tasas de interés y una lista de clientes. Implementa métodos para abrir una cuenta
# bancaria para un cliente y calcular los intereses acumulados en base a las tasas de interés.
class Cliente():
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

class Banco():
    def __init__(self, nombre):
        self.nombre = nombre
        self.tasa = 15
        self.lista_clientes = []
    def agregar (self, cliente):
        self.lista_clientes.append(cliente)
    def intereses (self,cliente):
        cliente.saldo += (cliente.saldo * self.tasa)/100
        return print(cliente.saldo)
    def mostrar (self):
        for cliente in self.lista_clientes:
            print(cliente.nombre, cliente.saldo)

banco1 = Banco("Frances")
op = "0"
while op !="4":
    print("Elija una opcion: \n 1.Para agregar cliente: \n 2.Para calcular intereses sumados: \n 3.Mostrar clientes: ")
    op = input("ingrese la opcion elegida: ")
    if op == "1":
        cliente1 = Cliente(input("Ingrese el nombre del cliente: "), int(input("Ingese el saldo del cliente: ")))
        banco1.agregar(cliente1)
    elif op == "2":
        banco1.intereses(cliente1)
    elif op == "3":
        banco1.mostrar()