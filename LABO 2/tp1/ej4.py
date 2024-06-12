# 4- Desarrollar una clase Cafetera con:
# • Atributos:
# ◦ capacidadMaxima: Cantidad máxima de café que puede contener la cafetera en CC
# ◦ cantidadActual: Cantidad actual de café que hay en la cafetera en CC
# • Métodos:
# ◦ Constructor: Considerar por defecto capacidad máxima de 1000 CC y cantidad actual en
# cero
# ◦ llenar(): Llena cafetera a la capacidad máxima
# ◦ servir(cantidad): sirve una cantidad de café (Verificar que cantidad sea positivo y no
# servir mas del actual)
# ◦ vaciar(): Vaciar cafetera
# ◦ agregar(cantidad): añade una cantidad de café (Verificar que cantidad sea positivo y no
# supere el máximo)

class Cafetera():
    def __init__(self):
        self.capmax = 1000
        self.cantac = 0

    def llenar (self):
        self.cantac = 1000
    def servir (self, cantidad):
        self.cantac -= cantidad
    def vaciar (self):
        self.cantac = 0
    def agregar (self, cantidad):
        if cantidad > 0 and (cantidad + self.cantac) <= self.capmax:
            self.cantac += cantidad
        else:
            return "Cantidad invalida: debe ser mayor a cero o no superar el limite."
        
cafetera1 = Cafetera()
print(cafetera1.cantac)
cafetera1.llenar()
print(cafetera1.cantac)
cafetera1.servir(500)
print(cafetera1.cantac)
cafetera1.vaciar()
print(cafetera1.cantac)
cafetera1.agregar(800)
print(cafetera1.cantac)
print(cafetera1.agregar(800))
print(cafetera1.agregar(0))