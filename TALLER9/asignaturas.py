def menu():
    bandera = True
    lista = []
    while bandera:
        try:
            print("\n1. Ingresar asignatura.\n2. Ver asignaturas registradas.\n0. Salir\n")
            opcion = int(input("Ingrese una opción del menú: "))
            if opcion == 0:
                bandera = False
            elif opcion == 1:
                lista = ingresarAsignatura()
            elif opcion == 2:
                print(lista)
            else:
                print("La opción no es válida.")    
        except ValueError:
            print("La opción no es válida.")

def ingresarAsignatura():
    lista = []
    banderaL = True
    while banderaL:
        asignatura = input("Ingrese asignatura (Para salir esciba SALIR): ")
        if asignatura == "SALIR":
            banderaL = False
        else:
            lista.append(asignatura)
    return lista

menu()