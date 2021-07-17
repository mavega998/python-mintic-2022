# Escribe un programa que pida la nota de un estudiante (de 1 a 10) y diga si es un
# insuficiente (menos de 5), suficiente (de 5 a 7), notable (de 7 a 9) o
# sobresaliente (entre 9 a 10) 2.
try:
    nota = float(input("Ingrese la nota: (1- 10)"))
    if nota <5:
        print("Insuficiente")
    elif 5 < nota < 7:
        print("Suficiente")
    elif 6 < nota < 9:
        print("Notable")
    else:
        print("Sobresaliente")
except ValueError:
    print("El valor no es válido")