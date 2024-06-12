class Triangulo():
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
    def perimetro (self):
        return self.ladoA + self.ladoB + self.ladoC
    def equilatero(self):
        return self.ladoA == self.ladoB and self.ladoB == self.ladoC
    def escaleno (self):
        return self.ladoA != self.ladoB and self.ladoB != self.ladoC
    def isosceles (self):
        return self.ladoA == self.ladoB and self.ladoB != self.ladoC

trian1 = Triangulo(4,4,4)
print("El triangulo es equilatero?: ",trian1.equilatero())
print("El triangulo es isosceles?: ", trian1.isosceles())
print("El triangulo es escaleno ?: ", trian1.escaleno())