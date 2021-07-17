edad = int(input("Ingrese su edad: "))
if edad == 0:
    print("No es una edad válida.")
elif edad >= 18:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")