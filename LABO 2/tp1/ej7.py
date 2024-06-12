class CuentaBanc():
    def __init__(self, apellido, nombre, num_cuenta):
        self.apellido = apellido
        self.nombre = nombre
        self.num_cuenta = num_cuenta
        self.saldo = 0
        self.listadohistorial = []
    def __str__(self):
        return f"{self.apellido}, {self.nombre}, {self.num_cuenta}, {self.saldo}"
    def saldofun(self):
        return self.saldo
    def ingresarmon(self, monto):
        if monto > 0:
            self.saldo += monto
            self.listadohistorial.append(f" +{monto}")
        else:
            return "Ingrese un numero mayor a 0"
    def retirarmon(self, monto):
        if monto > 0 and monto < self.saldo:
            self.saldo -= monto
            self.listadohistorial.append(f" -{monto}")
        else:
            return "Saldo insuficiente o valor invalido"
    def historial (self):
        for histo in self.listadohistorial:
            print(histo)


cuenta1 = CuentaBanc("Diaz", "Franco", 234,)
cuenta1.ingresarmon(400)
print(cuenta1)
print(cuenta1.retirarmon(500))
cuenta1.ingresarmon(900)
cuenta1.ingresarmon(300)
cuenta1.ingresarmon(200)
cuenta1.ingresarmon(1300)
cuenta1.retirarmon(300)
cuenta1.retirarmon(900)
cuenta1.historial()
#INCORPORAR A LA CLASE ANTERIOR UNA LISTA CON EL HISTORIAL DE INGRESOS
#  Y RETIROS DE LA CUENTA. AGREGAR 
# EL METODO HISTORIAL QUE MUESTRE MOVIMIENTOS