# 1. Figuras Geométricas:
#  - Clase Padre: 'Figura'
#  - Atributos: cantidad_lados: contiene la cantidad de lados
#  - Métodos: Ninguno
#  - Clase Hija: 'Círculo'
#  - Atributos:
#  - 'radio': Radio del círculo.
#  - Métodos:
#  - 'calcular_area()': Calcula el área del círculo usando la fórmula πr².
#  - 'calcular_perimetro()': Calcula el perímetro del círculo usando la fórmula 2πr.
#  - Clase Hija: 'Triángulo'
#  - Atributos:
#  - 'base': Longitud de la base del triángulo.
#  - 'altura': Altura del triángulo.
#  - Métodos:
#  - 'calcular_area()': Calcula el área del triángulo usando la fórmula 0.5 * base * altura.
#  - 'calcular_perimetro()': Calcula el perímetro del triángulo sumando las longitudes de sus lados.
#  - Clase Hija: 'Cuadrado'
#  - Atributos:
#  - 'lado': Longitud de un lado del cuadrado.
#  - Métodos:
#  - 'calcular_area()': Calcula el área del cuadrado multiplicando el lado por sí mismo.
#  - 'calcular_perimetro()': Calcula el perímetro del cuadrado multiplicando el lado por 4.
import math
class Figura():
    def __init__(self, lados):
        self.lados = lados
    
class Circulo(Figura):
    def __init__(self, lados, radio):
        super().__init__(lados)
        self.radio = radio
    def areac (self):
        return f"El area del circulo es: {math.pi*(self.radio**2)}"
    def perimetro (self):
        return f"El perimetro del circulo es:{2*math.pi*self.radio}"
class Triangulo(Figura):
    def __init__(self, lados, base, altura, ladoa, ladob, ladoc):
        super().__init__(lados)
        self.base = base
        self.altura = altura
        self.ladoa = ladoa
        self.ladob = ladob
        self.ladoc = ladoc
    def areat (self):
        return f"El area del triangulo es: {0.5 * self.base * self.altura}"
    def perimetrot(self):
        return f"El perimetro del triangulo es: {self.ladoa + self.ladob + self.ladoc}"
class Cuadrado (Figura):
    def __init__(self, lados, lado):
        super().__init__(lados)
        self.lado = lado
    def areacu (self):
        return f"El area del cuadrado es: {self.lado**2}"
    def perimetrocu(self):
        return f"El perimetro del cuadrado es: {self.lado * 4}"

circulo1 = Circulo(0, 4)
print(circulo1.areac(), "\n", circulo1.perimetro())
triangulo1 = Triangulo(3, 4, 2.5, 3, 4, 5)
print(triangulo1.areat(), "\n",triangulo1.perimetrot())
cuadrado1 = Cuadrado(4, 3)
print(cuadrado1.areacu(), "\n", cuadrado1.perimetrocu())