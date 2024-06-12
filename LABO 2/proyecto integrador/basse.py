class Fecha ():
    def __init__(self, hora):
        self.fechas = []
        self.hora = hora
    def __str__(self):
        return f"{self.fechas} {self.hora}"

    def agregarfe (self, fe):
        self.fechas.append(fe)

class Butaca ():
    def __init__(self):
        self.butaca = []
    
    def agregarbu (self, bu):
        self.butaca.append(bu)

    def __str__(self):
        return f"{self.butaca}"
class Hora ():
    def __init__(self, butaca):
        self.hora = []
        self.butaca = butaca
    def agregarho (self, ho):
        self.hora.append(ho)

    def __str__(self):
        return f"{self.hora} {self.butaca}"


class Destino ():
    def __init__(self, fecha, hora, butaca):
        self.destino = []
        self.fecha = fecha
        self.hora = hora
        self.butaca = butaca
    def agregardes (self, des):
        self.destino.append(des)


class Viaje ():
    def __init__(self, fecha, hora, butaca):
        self.destino = []
        self.fecha = fecha
        self.hora = hora
        self.butaca = butaca
butacaba = Butaca ()
butacaba.agregarbu(1)
butacaba.agregarbu(2)
butacaba.agregarbu(3)
butacaba.agregarbu(4)
butacaba.agregarbu(5)
butacaba.agregarbu(6)
butacaba.agregarbu(7)
butacaba.agregarbu(8)
butacaba.agregarbu(9)
horaba = Hora(butacaba)
horaba.agregarho (00)
horaba.agregarho(14)
horaba.agregarho(22)
fechaba = Fecha(horaba)
fechaba.agregarfe ("12/01")
fechaba.agregarfe ("13/01")
fechaba.agregarfe ("14/01")
buenosaires = Destino (fechaba, horaba, butacaba)
buenosaires.agregardes("Buenos Aires")
print(fechaba)