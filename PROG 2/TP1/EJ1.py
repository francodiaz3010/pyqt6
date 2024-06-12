#Construye una clase llamada Estudiante con los siguientes atributos:
#- nombre: El nombre del estudiante.
#- edad: La edad del estudiante.
#- promedio: El promedio de calificaciones del estudiante.
#- carrera: La carrera que está estudiando.
#La clase debe tener los siguientes métodos:
#1. verificar_aprobacion(self): Este método debe verificar si el estudiante ha aprobado. Si
#el promedio es mayor o igual a 70, debe retornar "Aprobado". En caso contrario, debe
#retornar "Reprobado".
#2. es_mayor_de_edad(self): Este método debe verificar si el estudiante es mayor de edad.
#Si la edad es mayor o igual a 18, debe retornar True. Si es menor, debe retornar False.

class Estudiante():
    def __init__(self, nombre, edad, promedio, carrera):
        self.nombre = nombre
        self.edad = edad 
        self.promedio = promedio
        self.carrera = carrera
    def verificar_aprobacion(self):
        condicion = 0
        if self.promedio >= 70:
            condicion = "Aprobado"
        else:
            condicion = "Reprobado"
        return condicion
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
estudiante1 = Estudiante("franco", 30, 90, "programacion")
estudiante2 = Estudiante("diego", 17, 50, "ed fisica")
print("La condicion del estudiantes es: ", estudiante1.verificar_aprobacion())
print("La condicion del estudiante es: ", estudiante2.verificar_aprobacion())
print("El estudiante es mayor de edad: ", estudiante1.es_mayor_de_edad())
print("El esstudiante es mayor de edad: ", estudiante2.es_mayor_de_edad())