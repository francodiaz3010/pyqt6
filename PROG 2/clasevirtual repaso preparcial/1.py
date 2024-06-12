class Persona():
    def __init__(self, nombre, apellido, edad, altura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura
        self.peso = peso
    def __str__(self):
        return f"El nombre es: {self.nombre}, apellido: {self.apellido}, su edad: {self.edad}, la altura: {self.altura} y su peso: {self.peso}"
    
    def mostañonac(self, año):
        return año - self.edad
class Alumno(Persona):
    def __init__(self, nombre, apellido, edad, carrera, matricula, año_ingreso, comision):
        super().__init__(nombre, apellido, edad, altura=None, peso=None)
        #del super().altura
        #del super().peso asi podemos borrar atributos.
        self.carrera = carrera
        self.matricula = matricula
        self.año_ingreso = año_ingreso
        self.comision = comision
        self.notas = []

    def calcularprom (self):
        return f"El promedio es: {(sum(self.notas)/len(self.notas))}"
    
    def antcarr (self, añoac):
        return añoac - self.año_ingreso
    
    def cargarnotas (self, nota):
        self.notas.append(nota)
    def __str__(self):
        return super().__str__() + f" carrera que cursa: {self.carrera}, la matricula es: {self.matricula}, la comision es: {self.comision}"

class AlumnoPrimaria(Persona):
    def __init__(self, nombre, apellido, edad, altura, peso, tutor):
        super().__init__(nombre, apellido, edad, altura, peso)
        self.tutor = tutor
        self.notas = []

    def agregarnota(self, nota):
        self.notas.append(nota)
    def calcpromedio(self):
        return f"El promedio es: {(sum(self.notas)/len(self.notas))}"
    def mostrar(self):
        return f"Datos del tutor a continuacion... {self.tutor}"
    def añoegreso(self,añoac):
        return f"El año de egreso es: {añoac + (13 -self.edad)}"

tutor1 = Persona("Maria", "gomez", 45, 1.66, 60)
alumnop1 = AlumnoPrimaria("carlitos", "merida", 8, 1.30, 45, tutor1)

print(alumnop1.mostrar())
print(alumnop1.añoegreso(2023))
alumnop1.agregarnota(10)
alumnop1.agregarnota(8)
print(alumnop1.calcpromedio())