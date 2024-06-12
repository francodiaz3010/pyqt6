# 6- Realizar una clase CuentaBancaria con los siguientes atributos y metodos:
# • Atributos: nombre del titular, apellido del titular, numero de cuenta, saldo de la cuenta.
# • Métodos:
# ◦ constructor: con saldo inicial en cero.
# ◦ __str__(): devolver todos los atributos.
# ◦ saldo(): mostrar el saldo de la cuenta
# ◦ ingresar(monto): ingresar un monto a la cuenta verificando monto positivo
# ◦ retirar(monto): retirar un monto a la cuenta verificando monto positivo
class CuentaBanc():
    def __init__(self, apellido, nombre, num_cuenta):
        self.apellido = apellido
        self.nombre = nombre
        self.num_cuenta = num_cuenta
        self.saldo = 0
        self.listadohistorial = []
    def __str__(self):
        return f"Apellido: {self.apellido}, \nNombre: {self.nombre}, \nNumero de cuenta: {self.num_cuenta}, \nSaldo en cuenta: {self.saldo}"
    def saldofun(self):
        return f"El saldo en la cuenta es: {self.saldo}"
    def ingresarmon(self, monto):
        if monto > 0:
            self.saldo += monto
        else:
            return "Ingrese un numero mayor a 0"
    def retirarmon(self, monto):
        if monto > 0 and monto < self.saldo:
            self.saldo -= monto
        else:
            return "Saldo insuficiente o valor invalido"
cuenta1 = CuentaBanc("Diaz", "Franco", 234,)
cuenta1.ingresarmon(400)
print(cuenta1)
print(cuenta1.retirarmon(500))
cuenta1.ingresarmon(900)
print(cuenta1.saldofun())
cuenta1.ingresarmon(300)
print(cuenta1.saldofun())
cuenta1.ingresarmon(200)
print(cuenta1.saldofun())
cuenta1.ingresarmon(1300)
print(cuenta1.saldofun())
cuenta1.retirarmon(300)
print(cuenta1.saldofun())
cuenta1.retirarmon(900)
print(cuenta1.saldofun())