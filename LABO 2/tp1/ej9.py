# 9- Realizar una clase que represente una estructura de datos de tipo ‘Cola’ con una lista como
# atributo. Incluir los siguientes métodos:
# • constructor: inicializa lista vacía.
# • agregar(): agrega un elementos al final de la lista.
# • quitar(): quita el primer elemento de la lista y lo devuelve.
# • estaVacia(): devuelve True si la lista esta vacía.
# • cantidad(): devuelve cantidad de elementos ingresados

class Cola():
    def __init__(self):
        self.lista = []
    
    def agregar (self, elemento):
        self.lista.append(elemento)
    def quitar(self):
        if len(self.lista) != 0:
            return f"elemento quitado: {self.lista.pop(0)}"
        else:
            return "Cola vacia."
    def estavacia (self):
        return f"La cola esta vacia?: {len(self.lista) == 0}"
    def cantidad(self):
        return f"La cantidad de elementos en la cola es: {len(self.lista)}"
    

cola1 = Cola()
print(cola1.estavacia())
print(cola1.quitar())
cola1.agregar(1)
cola1.agregar(2)
cola1.agregar(3)
print(cola1.lista)
print(cola1.quitar())
print(cola1.lista)
cola1.agregar(10000)
print(cola1.quitar())
print(cola1.estavacia())
print(cola1.cantidad())
print(cola1.lista)