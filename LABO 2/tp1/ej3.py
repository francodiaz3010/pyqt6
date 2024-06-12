# 3- Realizar una clase Contador con un atributo llamado cuenta. Implementar los siguientes métodos:
# • Constructor con cuenta opcional iniciada en cero.
# • mostrar(): Mostrar en pantalla la cuenta actual
# • incrementar(valor): Incrementar la cuenta en valor o por defecto en 1 si no se especifica
# valor.
# • decrementar(valor): Decrementar la cuenta en valor o por defecto en 1 si no se especifica
# valor.
# • reiniciar(): Reinicar la cuenta a cero.


class Contador():
    def __init__(self, cuenta=0):
            self.cuenta = cuenta

    def mostrar(self):
        return self.cuenta
    def incrementar(self,valor = None):
        if valor is None:
            self.cuenta += 1
        else:
            self.cuenta = self.cuenta + valor
    def decrementar (self, valor = None):
        if valor is None:
            self.cuenta -= 1
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