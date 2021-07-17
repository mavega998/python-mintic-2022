try:
    numero = int(input("Ingrese número: "))
    if numero >= 0:
        for i in range(numero):
            if (i % 2) != 0:
                print(i)
    else:
        print("Debe ser un número positivo.")
except ValueError:
    print("Valor no válido.")