# 5- Escribir una clase Persona con los siguientes atributos y métodos:
# • Atributos: nombre, apellido, edad en años, altura en metros y peso en Kg.
# • Métodos:
# ◦ constructor,
# ◦ nombreCompleto(): Retorna apellido y nombre con formato: ‘apellido, nombre’
# ◦ esMayor(): Retorna True si la persona tiene 18 años o más.
# ◦ imc(): Retorna indice de masa corporal de la persona
# ◦ __str__(): Retorna todos los atributos separados por coma.

class Persona():
    def __init__(self, nombre, apellido, edad, altura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura
        self.peso = peso
    
    def __str__ (self):
        return f"{self.nombre}, {self.apellido}, {self.edad}, {self.altura}, {self.peso}."
    def nombrecompleto(self):
        return f"Apellido: {self.apellido} \nNombre: {self.nombre}"
    def esmayor (self):
        return f"\nEs mayor?: {self.edad >= 18}"
    def imc (self):
        im = self.peso/(self.altura**2)
        return f"\nEl indice de masa corporal es: {im}"
    


persona1 = Persona("Franco", "Diaz", 30, 1.77, 62)
print(persona1)
print(persona1.nombrecompleto(), persona1.esmayor(), persona1.imc())