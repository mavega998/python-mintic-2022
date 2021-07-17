bandera = True
lista = []

while bandera:
    try:
        numero = int(input("Ingrese número (0 para salir): "))
        if numero == 0:
            bandera = False
        else:
            lista.append(numero)
    except ValueError:
        print("No es un número.")

lista2 = lista
lista2.sort(reverse=True)
print(lista2)
print(sorted(lista, reverse=True))