class Contador():
    def __init__(self, cuenta=0):
        self.cuenta = cuenta
    def mostrar(self):
        return self.cuenta
    def incrementar(self,valor = None):
        if valor is None:
            self.cuenta = self.cuenta + 1
        else:
            self.cuenta = self.cuenta + valor
    def decrementar (self, valor = None):
        if valor is None:
            self.cuenta = self.cuenta - 1
        else:
            self.cuenta = self.cuenta - valor
    def reiniciar (self):
        self.cuenta = 0
num = Contador()
print(num.mostrar())
num.incrementar()
print(num.mostrar())
num.incrementar(5)
print(num.mostrar())
num.decrementar()
print(num.mostrar())
num.decrementar(3)
print(num.mostrar())
num.reiniciar()
print(num.mostrar())