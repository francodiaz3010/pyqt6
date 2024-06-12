# `6) Clase: ProductoElectrónico
# Diseña una clase ProductoElectrónico que represente un producto electrónico. Define los
# atributos necesarios para el nombre, marca, precio y disponibilidad del producto. Crea métodos
# para simular la compra del producto, cambiando su estado de disponibilidad, y para verificar la
# garantía en caso de defectos.`
class ProdElec():
    def __init__(self,nombre, marca, precio):
        self.nombre =  nombre
        self.marca = marca
        self.precio = precio
        self.disp = True
    def compra (self):
        self.disp = False
    def garantia (self, meses_compra):
        print("garanita disponible: ")
        return meses_compra < 4
    
prod1 = ProdElec("bordeadora", "stihl", 70000)

print(prod1.disp)
prod1.compra()
print(prod1.disp)
print(prod1.garantia(6))