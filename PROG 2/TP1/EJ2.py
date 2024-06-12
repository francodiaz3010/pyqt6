#2) Clase: Libro
#Crea una clase llamada Libro con los siguientes atributos:
#- título: El título del libro.
#- autor: El autor del libro.
#- año_publicación: El año en que se publicó el libro.
#- disponible: Un booleano que indica si el libro está disponible para préstamo.
#La clase debe tener los siguientes métodos:
#1. solicitar_prestamo(self): Este método debe cambiar el estado del libro a no disponible y
#retornar un mensaje indicando que el libro ha sido prestado, siempre y cuando esté
#disponible. Si no está disponible, debe retornar un mensaje indicando que el libro no
#puede ser prestado en ese momento.
#2. devolver_libro(self, días): Este método recibe la cantidad de días que el libro ha sido
#prestado y calcula una posible multa si se ha excedido el tiempo de préstamo. Si no hay
#multa, debe retornar un mensaje indicando que el libro ha sido devuelto.
import time
time.sleep(20)
class Libro():
    def __init__(self, titulo, autor, año_pub):
        self.titulo = titulo
        self.autor = autor
        self.año_pub = año_pub
        self.disponible = True
    def solicitar_prestamo(self):
        if self.disponible == True:
            self.disponible = False
            return "Libro disponible para el prestamo."
        else:
            return "Libro no disponible."
    def devolver_libro(self, dias):
        self.disponible = True
        if dias > 30:
            return "Usted debe pagar una multa equivalente a 14$ por dia de atraso"
        else:
            return "Libro devuelto."

libro1 = Libro("ojos", "juan", 2020)
libro2 = Libro("perro", "Diego", 2021)
print(libro1.solicitar_prestamo())
print(libro1.solicitar_prestamo())