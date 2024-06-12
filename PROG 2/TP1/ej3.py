# 3) Clase: TiendaOnline
# Escribe una clase llamada TiendaOnline con los siguientes atributos:
# - nombre_tienda: El nombre de la tienda en línea.
# - productos_disponibles: Una lista de productos disponibles en la tienda.
# - ubicación: La ubicación de la tienda en línea.
# - ventas_mensuales: El total de ventas mensuales de la tienda.
# La clase debe tener los siguientes métodos:
# 1. buscar_producto(self, producto): Este método debe buscar un producto en la lista de
# productos disponibles y retornar su información si se encuentra. Si no se encuentra, debe
# retornar un mensaje indicando que el producto no está disponible en este momento.
# 2. calcular_descuento(self, monto_compra): Este método debe calcular un descuento en
# base al monto de compra. Si el monto es mayor o igual a $100, debe aplicar un
# descuento del 10%. Si es mayor o igual a $200, debe aplicar un descuento del 20%. Debe
# retornar el monto total con el descuento aplicado.

class Tienda ():
    def __init__(self, nombre, productos, ubicacion, ventas):
        self.nombre = nombre
        self.productos = productos
        self.ubicacion = ubicacion
        self.ventas = ventas

    def buscar(self, prod):
                if prod in self.productos:
                    return f"El producto esta disponible y su precio es: {self.productos.get(prod)}"
                else:
                    return "Producto no disponible"
    def descuento(self, monto):
        descuento = 0
        if monto >= 100:
            descuento = 0.10
        elif monto >= 200:
            descuento = 0.20
        
        des_total = monto * descuento
        monto_total = monto - des_total
        return f"El monto total con el descuento aplicado es: {monto_total}"

tienda1 = Tienda("Roma", {"remera" : 4000, "pantalon" : 12000, "buzo" : 20000}, "San nicolas de bari 668", 2000000)

print(tienda1.buscar("remera"))
print(tienda1.descuento(160))

