class Cancion():
    def __init__(self, titulo, autor, duracion):
        self.titulo = titulo 
        self.autor = autor 
        self.duracion = duracion

    def __str__(self):
        return f"El titulo es{self.titulo}, su autor: {self.autor} y la duracion es: {self.duracion}"

class Album():
    def __init__(self, titulo):
        self.titulo = titulo
        self.canciones = []
    def agregarcancion (self, cancion):
        self.canciones.append(cancion)

    def numerocancion(self):
        return len(self.canciones)
    
    def eliminarcancion(self, indice):
        self.canciones.pop(indice)

    def duraciontotal (self):
        duracionto = 0
        for cancio in self.canciones:
            duracionto += cancio.duracion 
        return duracionto
    def __str__(self):
        str = ""
        for i in range(len(self.canciones)):
            str += f" Pista: {i+1} => {self.canciones[i]}\n"
        return str
        
cancion0 = Cancion("A", "0", 15)
cancion1 = Cancion("B", "1", 20)
cancion2 = Cancion("C", "2", 30)

album = Album("Primer Album")
album.agregarcancion(cancion0)
album.agregarcancion(cancion1)
album.agregarcancion(cancion2)

print(album.duraciontotal())