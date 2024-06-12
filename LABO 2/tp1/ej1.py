# 1- Escribir un programa en Python que cree una clase representando un circulo. Emplear radio
# como atributo e incluir métodos para calcular su área y perímetro.
import math
class Circulo():
    def __init__(self, radio):
        self.radio = radio
    
    def area (self):
        return f"\n El area del circulo es: {math.pi * (self.radio**2)}"
    def perimetro (self):
        return f"El perimetro del circulo es: {2 * math.pi * self.radio}"
    
circulo1 = Circulo (6)
print(circulo1.perimetro(), circulo1.area())