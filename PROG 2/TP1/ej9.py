# 9) Clase: Empleado
# Diseña una clase Empleado que almacene información sobre los empleados de una empresa.
# Define atributos para el nombre, edad, salario y cargo del empleado. Crea métodos para calcular
# y aplicar aumentos salariales en base a un porcentaje y para cambiar el cargo del empleado.

class Empleado():
    def __init__(self, nombre, edad, salario, cargo):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.cargo = cargo

    def aumento (self, porcentaje):
        self.salario = self.salario + (self.salario * (porcentaje/100))
    def ascenso (self):
        if self.cargo == "obrero":
            self.cargo = "supervisor"
        elif self.cargo == "supervisor":
            self.cargo = "jefe"
        else:
            self.cargo = "Maximo rango obtenido, gracias vuelva prontos."

empleado1 = Empleado("Juan Perez", 25, 50000, "obrero")
empleado1.ascenso()
print(empleado1.cargo)
empleado1.aumento(50)
print(empleado1.salario)
empleado1.ascenso()
empleado1.ascenso()
print(empleado1.cargo)