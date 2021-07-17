def dicCuadrado(n):
    i = 0
    diccionario = {}
    while (i < n):
        diccionario[i] = i**2
        i += 1
    return diccionario

print(dicCuadrado(10))