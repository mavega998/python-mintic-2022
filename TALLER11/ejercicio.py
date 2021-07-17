from random import random

def menu():
    print("---- Menú de Opciones ----")
    print("1. Contar repetidos en la tupla.\n2. Mayor y menor de la tupla.\n3. Lista de telefonos.")
    print("4. Datos en tupla.\n5. Suma y media de lista.\n6. Tupla de meses.\n0. Salir.\n")
    bandera = True
    while bandera:
        try:
            opcion = int(input("Elija una opción del menú: "))
            if opcion == 0:
                bandera = False
            elif opcion == 1:
                contarRepetidos()
        except ValueError:
            print("No es una opción válida.")

def contarRepetidos():
    tupla = []
    size = int(random() * 100)
    i = 0
    while i< size:
        tupla.append(int(random * 10))
        i += 1
    print(tupla)

menu()