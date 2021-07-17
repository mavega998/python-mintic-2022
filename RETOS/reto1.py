sueldo = int(input("Ingrese salario: "))
alimentos = sueldo * 0.30
pasajes = sueldo * 0.15
cine = sueldo * 0.10
libros = sueldo * 0.15
alquiler = sueldo - alimentos - pasajes - cine - libros

print(alquiler)