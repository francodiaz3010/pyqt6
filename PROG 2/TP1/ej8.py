# 8) Clase: Restaurante
# Crea una clase Restaurante para representar un lugar de comida. Define atributos para el
# nombre del restaurante, tipo de cocina, cantidad de mesas disponibles y valoración. Implementa
# métodos para permitir a los clientes reservar mesas y calificar el restaurante, actualizando su
# valoración

class Restaurante:
    def __init__(self, nombre, tipo, mesas):
        self.nombre = nombre
        self.tipo = tipo
        self.mesas = mesas
        self.valoracion = 5
        self.cantidad = 10
    def reserva(self, cantidad):
        self.mesas = self.mesas - cantidad
        return f"Reserva recibida, cantidad de mesas disponibles: {self.mesas}"
    def valorar(self, puntos):
        desprome = (self.valoracion * self.cantidad) + puntos
        self.cantidad += 1
        calculo = desprome / self.cantidad
        self.valoracion = calculo


restaurante1 = Restaurante("gallo", "Comida china", 45)
print(restaurante1.reserva(4))
restaurante1.valorar(4)
print(f"la valoracion del resto es: {restaurante1.valoracion} estrellas")