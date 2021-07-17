try:
    n1 = int(input("Ingrese número 1 (n1): "))
    n2 = int(input("Ingrese número 2 (n2): "))
    n3 = int(input("Ingrese número 3 (n3): "))

    if n1 < 10 and n2 < 10 and n3 < 10:
        print("Todos son menores a 10.")
    elif n1 < 10 and n2 < 10:
        print("Solo n1 y n2 son menores a 10.")
    elif n2 < 10 and n3 < 10:
        print("Solo n2 y n3 son menores a 10.")
    elif n1 < 10 and n3 < 10:
        print("Solo n1 y n3 son menores a 10.")
    elif n1 < 10 or n2 < 10 or n3 < 10:
        print("Algún número es menor a 10.")
    else:
        print("Ninguno es menor a 10.")
except ValueError:
    print("Valor no válido.")