class Motor ():
    def __init__(self, aceite, temp):
        self.aceite = aceite
        self.temp = temp
        self.encendido = False
        
    def arrancar(self):
        if self.encendido == False:
            self.encendido = not self.encendido
            return f"Motor encendido."
        else:
            f"Motor ya encendido, no se puede sobreencender."
    def detener(self):
        if self.encendido == True:
            self.encendido = not self.encendido
            return f"Motor apagado."
        else:
            return f"Motor ya apagado."
    def __str__(self):
        return f"El nivel de aceite es: {self.aceite}, la temperatura es: {self.temp}. Esta encendido?: {self.encendido}."
class Rueda():
    

auto1 = Motor(4.5, 30)
auto1.arrancar()
print(auto1)