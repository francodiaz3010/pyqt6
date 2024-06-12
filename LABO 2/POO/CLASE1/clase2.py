class objeto():
    def __init__(self, atributo):
        self.atributo = atributo
    def mostrar (self):
        print(self.atributo)

obj = objeto (5) #obj va a ser una instancia que creamos con el objeto de la clase
print(obj.atributo)
obj.mostrar()