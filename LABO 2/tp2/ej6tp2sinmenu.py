class Libro ():
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor 
        self.paginas = paginas

    def __str__(self):
        return f"El titulo del libro es: {self.titulo}, su autor: {self.autor} y la cantidad de paginas: {self.paginas}"
    
class Biblioteca ():
    def __init__(self):
        self.libros = []

    def agregar (self, libro):
        self.libros.append(libro)

    def ordenar (self):
        aux = ""
        n = len(self.libros)
        for i in range(n):
            for j in range(i+1,n):
                if self.libros[i].titulo > self.libros[j].titulo:
                    aux = self.libros[i].titulo
                    self.libros[i].titulo = self.libros[j].titulo
                    self.libros[j].titulo = aux
    # def ordenar (self):
    #     sorted (self.libros, key= lambda x: x.titulo)
    
    def cantidad (self):
        return len(self.libros)
    
    def eliminar (self, indice):
        self.libros.pop(indice)
    
    def __str__(self):
        str = ""
        for i in range(len(self.libros)):
            str += f"El libro {i+1} corresponde a {self.libros[i].titulo} \n"
        return str
    
libro1 = Libro("C", "A", 190)
libro2 = Libro("D", "B", 300)
libro3 = Libro("A", "C", 400)

biblio1 = Biblioteca()
biblio1.agregar(libro1)
biblio1.agregar(libro2)
biblio1.agregar(libro3)
biblio1.ordenar()
print(biblio1)