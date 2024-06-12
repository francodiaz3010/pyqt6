# 2- Realizar un programa en Python que cree una clase que represente un triángulo.
# • Atributos: ladoA, ladoB y ladoC.
# • Métodos:
# ◦ perímetro(): devuelve perimetro del triángulo.
# ◦ esEquilatero(): retorna True si los tres lados son iguales.
# ◦ esIsosceles(): retorna True si dos lados son iguales y uno distinto.
# ◦ esEscaleno(): retorna True si los tres lados iguale son distintos.

class Triangulo():
    def __init__(self, ladoa, ladob, ladoc):
        self.ladoa = ladoa
        self.ladob = ladob
        self.ladoc = ladoc

    def perimetro (self):
        return f"El perimetro del triangulo es: {self.ladoa + self.ladob + self.ladoc}"
    def equilatero (self):
        return f"\nEs esquilatero?: {self.ladoa == self.ladob and self.ladob == self.ladoc}"
    def isosceles (self):
        return f"\nEs isosceles?: {self.ladoa == self.ladob and self.ladob != self.ladoc}"
    def escaleno (self):
        return f"\nEs escaleno?: {self.ladoa != self.ladob and self.ladob != self.ladoc}"
    
triangulo1 = Triangulo(3,3,3)
triangulo2 = Triangulo(3,3,4)
trianqulo3 = Triangulo(3,4,5)
print(triangulo1.perimetro(), triangulo1.equilatero(), triangulo1.isosceles(), triangulo1.escaleno())
print(triangulo2.perimetro(), triangulo2.equilatero(), triangulo2.isosceles(), triangulo2.escaleno())
print(trianqulo3.perimetro(), trianqulo3.equilatero(), trianqulo3.isosceles(), trianqulo3.escaleno())