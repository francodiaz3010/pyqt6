# 8- Realizar una clase que represente una estructura de datos de tipo ‘Pila’ con una lista como
# atributo. Incluir los siguientes métodos:
# • constructor: inicializa lista vacía.
# • agregar(): agrega un elementos al final de la lista.
# • quitar(): quita el último elemento de la lista y lo devuelve.
# • estaVacia(): devuelve True si la lista esta vacía.
# • cantidad(): devuelve cantidad de elementos ingresados

class Pila():
    def __init__(self):
        self.lista = []
    
    def agregar (self, elemento):
        self.lista.append(elemento)
    def quitar(self):
        if len(self.lista) != 0:
            return f"elemento quitado: {self.lista.pop()}"
        else:
            return "Lista vacia."
    def estavacia (self):
        return f"La lista esta vacia?: {len(self.lista) == 0}"
    def cantidad(self):
        return f"La cantidad de elementos en la lista es: {len(self.lista)}"
    
pila1 = Pila()
print(pila1.estavacia())
print(pila1.quitar())
pila1.agregar(1)
pila1.agregar(2)
pila1.agregar(3)
print(pila1.lista)
print(pila1.quitar())
print(pila1.lista)
pila1.agregar(10000)
print(pila1.quitar())
print(pila1.estavacia())
print(pila1.cantidad())