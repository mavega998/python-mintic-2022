# Un año es bisiesto si es divisible por 4, excepto si es una centuria, que tiene que ser divisible por
# 400 (1800 y 1900 no fueron bisiestos, pero 1600 y el 2000 sí). Escribe un programa que pida el número
# de un año y muestre si es bisiesto o no.
try:
    anio = int(input("Ingrese el año: "))
    if ((anio % 4) == 0) and ((anio % 100)!= 0) or ((anio % 400) == 0):
        print("Año bisiesto")
    else:
        print("Año no bisiesto")
except ValueError:
    print("No es un valor válido")