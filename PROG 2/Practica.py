#Modelar una clase que se llame circunferencia, dicha clase tiene como atributo el radio y como metodos el calculo
# de su perimetro y area.
import math

class Circunferencia():
    def __init__(self, radio):
        self.radio = radio
    def perimetro(self):
        per = 2 * (math.pi) * self.radio
        return per
    def area(self):
        ar = math.pi * (self.radio**2)
        return ar
circulo1 = Circunferencia(5)
print(circulo1.perimetro())
print(circulo1.area()) 