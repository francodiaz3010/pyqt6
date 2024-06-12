tupla = ("a", "palabra", "Franco")

print(tupla[-2:])

for t in tupla:
    print (t)


def operaciones (a,b):
    suma = a + b
    resta = a - b
    return suma, resta

print(operaciones(8,4))

#Muchas funciones no returnan tuplas

#Ahora si yo solo quiero devolver la suma...

resultado = (operaciones(4,5))
print("suma", resultado[0])
print("resta ", resultado[1])
rsuma, rresta = operaciones(8,8)

#Se puede acceder a cada indice de la tupla poniendo multivariables separados con coma y le va a corresponder a cada valor la posicion correspondiente de cada multivariable
print("La sumas es: ", rsuma)
print("La resta es: ", rresta)
