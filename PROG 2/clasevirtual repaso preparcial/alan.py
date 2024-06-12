#9) Clase: Empleado
#Diseña una clase Empleado que almacene información sobre los empleados de una empresa.
#Define atributos para el nombre, edad, salario y cargo del empleado. Crea métodos para calcular
#y aplicar aumentos salariales en base a un porcentaje y para cambiar el cargo del empleado.


class Empleado:
    def __init__(self,edad,nombre,salario,carggo):
        self.edad = edad
        self.nombre = nombre
        self.salario= salario
        self.cargo = carggo
    
    def reemplazodecargo(self):
        if self.cargo == "nuevo":
            self.cargo = "veterano"
        elif self.cargo == "veterano":
            self.cargo = "supervisor"
        elif self.cargo == "supervisor":
            self.cargo = "gerente"
        else: 
            self.cargo = "el maximo cargo adquirido"
        return self.cargo
    def aumento (self,porcentaje):
        actual = self.salario + (porcentaje*100/porcentaje)
        return f"el salario actual es {self.salario} , y por el aumento del {porcentaje},el salario queda en {actual}"


alan = Empleado(22,"alan",22000,"veterano")
print(alan.cargo)
alan.reemplazodecargo()
print(alan.cargo)
alan.reemplazodecargo()
print(alan.cargo)
alan.reemplazodecargo()
print(alan.cargo)