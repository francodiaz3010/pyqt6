class TiendaOnline:
    def __init__(self, nombre_tienda, ubicacion):
        self.nombre_tienda = nombre_tienda
        self.productos_disponibles = []
        self.ubicacion = ubicacion
        self.ventas_mensuales = 0

    def agregar_producto(self, producto):
        self.productos_disponibles.append(producto)

    def buscar_producto(self, producto):
        for prod in self.productos_disponibles:
            if prod['nombre'] == producto:
                return prod
        return "El producto no está disponible en este momento."

    def calcular_descuento(self, monto_compra):
        descuento = 0
        if monto_compra >= 200:
            descuento = 0.20
        elif monto_compra >= 100:
            descuento = 0.10

        monto_descuento = monto_compra * descuento
        monto_total = monto_compra - monto_descuento

        return monto_total

# Ejemplo de uso:
tienda = TiendaOnline("MiTiendaOnline", "Ciudad")
tienda.agregar_producto({"nombre": "Producto1", "precio": 50})
tienda.agregar_producto({"nombre": "Producto2", "precio": 150})
producto_buscado = tienda.buscar_producto("Producto1")
print(producto_buscado)