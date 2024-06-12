def filtro(lista):
    nueval = []
    for n in lista:
        if not isinstance(n, str):
            nueval.append(n)
    return nueval

lista1 = ["hola", 1, 2, "3", 3, "4", "cuatro"]

print(filtro(lista1))