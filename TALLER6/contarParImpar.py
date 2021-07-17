bandera = True
pares = 0
impares = 0
while bandera:
    try:
        numero = int(input("Ingrese un número positivo (Para salir ingrese 0): "))
        if numero == 0:
            bandera = False
            print("Cantidad de pares ", pares)
            print("Cantidad de impares ", impares)
        elif numero < 0:
            print("El número no es positivo.")
        else:
            if (numero % 2) == 0:
                pares += 1
            else:
                impares += 1
            print("En este momento hay ", pares, " pares")
            print("En este momento hay ", impares, " impares")
    except ValueError:
        print("Valor no válido.")