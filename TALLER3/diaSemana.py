semana = [
    {"id": 0,"name": 'domingo'},
    {"id": 1,"name": 'lunes'},
    {"id": 2,"name": 'martes'},
    {"id": 3,"name": 'miercoles'},
    {"id": 4,"name": 'jueves'},
    {"id": 5,"name": 'viernes'},
    {"id": 6,"name": 'sabado'},
]

opcionValor = input("1. Buscar el número del día por nombre.\n2. Buscar el nombre del día por el nombre.\n")
if opcionValor == '':
    print("Debe ingresar una opción.")
elif int(opcionValor) == 1:
    nombre = input("Ingrese el nombre: ")
    if nombre == '':
        print("El nombre no es válido.")
    else:
        for i in range(0, len(semana)):
            if nombre == semana[i].get("name"):
                print(semana[i].get("id"))
                break
elif int(opcionValor) == 2:
    número = input("Ingrese el número: ")
    if número == '':
        print("El número no es válido.")
    else:
        for i in range(0, len(semana)):
            if int(número) == semana[i].get("id"):
                print(semana[i].get("name"))
                break
else:
    print("No es una opción válida.")