def menu():
    total = 0
    bandera = True
    while bandera:
        try:
            num = int(input("Ingrese número: "))
            if num != 0:
                total = suma(total, num)
            else:
                bandera = False
                print(f"El total es {total}")
                sumaDigito = 0
                for i in str(total):
                    sumaDigito += int(i)
                print(f"La suma de los dígitos es {sumaDigito}")
        except ValueError:
            print("Valor no válido.")

def suma(total, num):
    return (total + num)

menu()