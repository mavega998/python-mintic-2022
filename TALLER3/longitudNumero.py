# numero = input("Ingrese el número: ")
# if len(numero) == 1:
#     print("Tiene ún dígito.")
# elif len(numero) == 2:
#     print("Tiene dos dígito.")
# elif len(numero) == 3:
#     print("Tiene tres dígito.")
# else:
#     print("No es un número válido.")
########################################
try:
    numero = int(input("Ingrese el número: "))
    if -10 < numero < 10:
        print("Es de un dígito.")
    elif -100 < numero < 100:
        print("Es de dos dígitos.")
    elif -1000 < numero < 1000:
        print("Es de tres dígitos.")
    else:
        print("No se puede procesar, tiene más de tres dígitos.")
except ValueError:
    print("No es un número válido.")