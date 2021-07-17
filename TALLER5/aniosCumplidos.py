try:
    edad = int(input("Ingrese su edad: "))
    for i in range(1, edad + 1):
        print("Cumplió " + str(i) + " año(s).")
except ValueError:
    print("Valor no válido")