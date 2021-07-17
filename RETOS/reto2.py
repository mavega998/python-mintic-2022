edad = int(input("Ingrese la edad (años): "))
peso = int(input("Ingrese peso (kg): "))
estatura = float(input("Ingrese altura (m): "))

if edad >= 20:
    imc = peso / (estatura**2);
    if imc < 17.5:
        print("Bajopeso")
    elif imc >= 17.5 and imc <=23.9:
        print("Normal")
    elif imc > 23.9 and imc <= 28.9:
        print("Sobrepeso")
    else:
        print("Obeso")
else:
    print("no tiene la edad")