# 10) Clase: AnimalDoméstico
# Modela una clase AnimalDoméstico que represente a un animal que puede ser una mascota.
# Define atributos para el nombre, especie, edad y dueño del animal. Implementa métodos para
# hacer un sonido característico de la especie y para verificar si el animal es joven, adulto o
# anciano en función de su edad y especie.

class AnimalDomestico():
    def __init__(self, nombre, especie, edad, dueño):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.dueño = dueño
    
    def sonido (self):
        if self.especie == "gato":
            return "MEOW"
        elif self.especie == "perro":
            return "WOOF WOOF"
        else:
            return "Yo soy tu padre"
    def juventud (self):
        if self.edad <= 10:
            return "Animal jr"
        elif self.edad > 10 & self.edad <= 20:
            return "Animal mid"
        else:
            return "Animal sennior"

mascota1 = AnimalDomestico ("Nina", "perro", 4, "Gladys")
mascota2 = AnimalDomestico ("Pupi", "gato", 15, "Alan")
mascota3 = AnimalDomestico ("oski", "pez", 23, "io")

print(mascota1.sonido(), mascota1.juventud())
print(mascota2.sonido(), mascota2.juventud())
print(mascota3.sonido(), mascota3.juventud())
