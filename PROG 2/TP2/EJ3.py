import math

class Animales ():
    def __init__(self, peso, edad):
        self.peso = peso
        self.edad = edad
    def __str__(self):
        return f"El peso es: {self.peso} y su edad: {self.edad}"
    
class Perro (Animales):
    def __init__(self, peso, edad, raza):
        super().__init__(peso, edad)
        self.raza = raza

    def edadhuman (self):
        return f"La edad humana de tu perro es: {16*(math.log(self.edad)) + 31} años."
        
class Gato (Animales):
    def __init__(self, peso, edad, pelaje):
        super().__init__(peso, edad)
        self.pelaje = pelaje

    def estsalud (self):
        if self.edad < 5 and self.peso > 5:
            return "Buen estado de salud para la edad de tu mascota."
        elif self.edad >= 5 and self.edad < 10 and self.peso > 7:
            return "Buen estado de salud para la edad de tu mascota"
        elif self.edad >=10 and self.edad < 20 and self.peso > 10:
            return "Buen estado de salud para la edad de tu mascota"
        else:
            return "Cheque medico proximo para tu mascota."
    def __str__(self):
        return super().__str__() + f" Su pelaje es: {self.pelaje}"    
perro1 = Perro (15, 10, "Doberman")
print(perro1)
print(perro1.edadhuman())

gato1 = Gato(15, 7, "Corto")
print(gato1)
print(gato1.estsalud())