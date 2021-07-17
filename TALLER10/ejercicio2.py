try:
    num = int(input("Ingrese número para generar tablas de multiplicar: "))
    lista = []
    for i in range(1, 11):
        lista.append(i*num)
    print(lista)
except ValueError:
    print("No es un número.")