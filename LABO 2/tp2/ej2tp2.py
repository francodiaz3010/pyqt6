class Inmueble():
    def __init__(self, id, canthab, sup, direccion, precio):
        self.id = id
        self.canthab = canthab
        self.sup = sup
        self.direccion = direccion 
        self.precio = precio
    def calcularpre(self, precarea):
        return f" El precio total es: {precarea * self.sup}"
    def __str__(self):
        return f"El identificador inmobiliario es: {self.id}, la cantidad de habitaciones: {self.canthab}, la superficie es: {self.sup} metros cuadrados. Se encuentra en la direccion: {self.direccion} y su precio es: {self.precio}"
    
class Casa(Inmueble):
    def __init__(self, id, canthab, sup, direccion, precio, cantpisos):
        super().__init__(id, canthab, sup, direccion, precio)
        self.cantpisos = cantpisos

    def __str__(self):
        return super().__str__() + f". La cantidad de pisos es {self.cantpisos}"
class Departamento(Inmueble):
    def __init__(self, id, canthab, sup, direccion, precio, numpiso):
        super().__init__(id, canthab, sup, direccion, precio)
        self.numpiso = numpiso
    def __str__(self):
        return super().__str__() + f". El numero del piso es: {self.numpiso}."
    
class CasaRural(Casa):
    def __init__(self, id, canthab, sup, direccion, precio, cantpisos, dismun, alt):
        super().__init__(id, canthab, sup, direccion, precio, cantpisos)
        self.dismun = dismun
        self.alt = alt
    def __str__(self):
        return super().__str__() + f". La dist a la muni mas cercana es: {self.dismun}, la altitud correspondiente es: {self.alt}"

class CasaUrbana(Casa):
    def __init__(self, id, canthab, sup, direccion, precio, cantpisos, pile):
        super().__init__(id, canthab, sup, direccion, precio, cantpisos)
        self.pile = pile
    
    def __str__(self):
        return super().__str__() + f". Tiende pileta??: {self.pile}"
    
class DeptoFliar(Departamento):
    def __init__(self, id, canthab, sup, direccion, precio, numpiso, cantfam):
        super().__init__(id, canthab, sup, direccion, precio, numpiso)
        self.cantfam = cantfam
    def __str__(self):
        return super().__str__() + f", la cantidad de fliares es: {self.cantfam}."
    
class DepartamentoEst(Departamento):
    def __init__(self, id, canthab, sup, direccion, precio, numpiso, cantemp):
        super().__init__(id, canthab, sup, direccion, precio, numpiso)
        self.cantemp = cantemp
    def __str__(self):
        return super().__str__() + f", y la cantidad de empelados es: {self.cantemp}."
    
casa1 = Casa(123, 4, 500, "San nicolas  de bari 668", 4500, 2)
print(casa1)
print(casa1.calcularpre(100))


departamento1 = Departamento(456, 5, 400, "San nicolas de bari 456", 4000, 3)
print(departamento1)

casa2 = CasaUrbana(896, 4, 500, "Rivadavia 123", 4500, 1, True)
print(casa2)