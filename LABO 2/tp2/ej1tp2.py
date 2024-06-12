class CuentaBanc():
    def __init__(self, apellido, nombre, saldo):
        self.apellido = apellido
        self.nombre = nombre
        self.saldo = saldo
    def __str__(self):
        return f"Apellido: {self.apellido}, Nombre: {self.nombre}, Saldo:{self.saldo}"
    def saldo(self):
        return self.saldo
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

class CuentaAhorro(CuentaBanc):
    def __init__(self, apellido, nombre, saldo):
        super().__init__(apellido, nombre, saldo)
        self.activa = self.saldo > 10000
    def ingresarmon(self, monto):
        if self.activa == True:
            return super().ingresarmon(monto)
        else:
            return "Cuenta inactiva"
    def retirarmon(self, monto):
        if self.activa == True:
            return super().retirarmon(monto)
        else:
            return "Cuenta inactiva"
    def __str__(self):
        return super().__str__() + f", cuenta activa: {self.activa}"
    
class CuentaCorriente(CuentaBanc):
    def __init__(self, apellido, nombre, saldo):
        super().__init__(apellido, nombre, saldo)
        self.sobregiro = 0

    def ingresarmon(self, monto):
        if self.sobregiro > 0:
            if monto < self.sobregiro:
                return f"Usted tiene un sobregiro de: {self.sobregiro}, ingrese un monto mayor por favor. "
            else:
                self.saldo += (monto - self.sobregiro)
        else:
            self.saldo += monto
    def retirarmon(self, monto):
        if monto > 0:
            if monto > self.saldo:
                self.saldo = (self.saldo - monto) 
                self.sobregiro = self.saldo * -1
            else:
                self.saldo -= monto
        else:
            return "Saldo negativo, no puede retirar."
    def __str__(self):
        return super().__str__() + f", tiene un sobregiro de: {self.sobregiro}"


cuenta1 = CuentaAhorro("Diaz", "Franco", 100)
print(cuenta1.ingresarmon(2000))
print(cuenta1)
cuentacorr1 = CuentaCorriente("Diaz", "Franco", 300)
cuentacorr1.retirarmon(500)
print(cuentacorr1)
print(cuentacorr1.ingresarmon(50))