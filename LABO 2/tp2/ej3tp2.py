class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Linea():
    def __init__(self, puntoa, puntob):
        self.puntoa = puntoa
        self.puntob = puntob
    def __str__(self):
        return f"La posicion de la linea es: punto a en x: {self.puntoa.x}, punto a en y: {self.puntoa.y}, punto b en x: {self.puntob.x}, punto b en y: {self.puntob.y}"

    def distancia(self):
        return f"La distancia en el eje x es: {self.puntoa.x - self.puntob.x}"
    
    def moverder(self, num):
        self.puntoa.x += num
        self.puntob.x += num
    def moverizq(self, num):
        self.puntoa.x -= num
        self.puntob.x -= num
    def moverarr (self, num):
        self.puntoa.y += num
        self.puntob.y += num
    def moveraba (self, num):
        self.puntoa.y -= num
        self.puntob.y -= num
    



a = Punto(10, 10)
b = Punto(5,15)
print
linea1 = Linea(a, b) #Los objetos puntos fotman parte de los atributos

print(linea1.puntoa.x)
print(linea1.puntoa.y)
print(linea1)
print(linea1.distancia())
linea1.moverder(5)
print(linea1)
linea1.moverizq(1)
print(linea1)
linea1.moveraba(90)
linea1.moverarr(2)
print(linea1)