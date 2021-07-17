try:
    palabra = input("Ingrese la palabra: ")
    numero = int(input("Ingrese la cantidad: "))

    for i in range(numero):
        print(palabra)
except ValueError:
    print("Valor no válido.")