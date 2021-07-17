bandera = True
sucesion = ""
while bandera:
    try:
        opcion = int(input("1. Serie de Fibonacci\n2. Salir\n"))
        if opcion == 1:
            n1 = 0
            n2 = 1
            numero = int(input("Longitud de la sucesión: "))
            for i in range(1, numero + 1 ):
                sucesion += str(n1) + " "
                aux = n1 + n2
                n1 = n2
                n2 = aux
            print("###########\n",sucesion,"\n###########\n")
        elif opcion == 2:
            bandera = False
            print("###########\nSaliendo...\n###########")
        else:
            print("###########\nNo es una opción válida.\n###########\n")
    except ValueError:
        print("###########\nValor no válido.\n###########\n")