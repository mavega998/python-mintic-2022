# SUPONGA que existen dos opciones para ser exonerados del parcial final:
#• Que las notas del parcial 1 y del proyecto sean mayores a 4.5.
#• Que en alguno de los dos parciales haya sacado 5.0 y el otro no lo haya perdido.

try:
    nota1 = float(input("Ingrese nota 1: (1.0 - 5.0)"))
    nota2 = float(input("Ingrese nota 2: (1.0 - 5.0)"))
    proyecto = float(input("Ingrese nota proyecto: (1.0 - 5.0)"))

    if (nota1 > 4.5 and proyecto > 4.5) or ((nota1 == 5.0 and nota2 >= 3.0) or (nota2 == 5.0 and nota1 >= 3.0)):
        print("Exonerado")
    else:
        print("No exonerado")
except ValueError:
    print("Valor nó válido")