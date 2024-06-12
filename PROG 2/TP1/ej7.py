# Modela una clase Película que almacene información sobre películas. Define atributos para el
# título, director, duración y género de la película. Implementa métodos para reproducir la película,
# mostrando su título y duración, y para recomendar la película a un usuario en base a su género
# preferido.

class Pelicula ():
    def __init__(self, titulo, director, duracion, genero):
        self.titulo = titulo
        self.director = director 
        self.duracion = duracion 
        self.genero = genero
    def repr (self):
        return print(f"Reproduciendo: {self.titulo} duracion: {self.duracion}")
    def recomendar (self, favorito):
        if favorito == self.genero:
            return print (f"En base a su genero favorito, la replicula recomendada es: {self.titulo}")

pelicula1 = Pelicula("felix", "juan", 120, "terror")

pelicula1.repr()
pelicula1.recomendar("terror")