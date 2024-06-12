class Persona:
    def __init__(self, apellido, nombre):
        self.nombre = nombre
        self.apellido = apellido
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
class Estudiante(Persona):
    #pass #Sirve para no dejar vacio, rellena
    def __init__(self, apellido, nombre, nota):
        super().__init__(apellido, nombre)
        self.nota = nota
    def __str__(self):
        #return f"{self.apellido}, {self.nombre}, {self.nota}"
        return super().__str__() + f", {self.nota}"
estudiante1 = Estudiante("Diaz", "Mercado", 10)
print(estudiante1)
persona1 = Persona("Diaz", "Paco")
print(persona1)