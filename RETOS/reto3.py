USER = "admin"
PSWD = "MisionTic2021"
bandera = False
fallas = 0

while fallas <= 3:
    usuario = input("Usuario: ")
    clave = input("Contraseña: ")
    if (usuario == USER) and (clave == PSWD):
        bandera = True
        fallas = 4
    else:
        fallas += 1
        print("Credenciales incorrectas")

empleados = ""
visitantes = ""

if (fallas == 4) and (bandera == False):
    print("Has agotado la cantidad de intentos, por favor inicie de nuevo el programa")

while bandera:
    print("\n------Menú de registro de personal-----")
    print("1. Registrar ingreso de empleado.\n2. Ver empleados ingresados.\n3. Registrar ingreso de visitantes.\n4. Ver visitantes ingresados.\n\n0. Salir\n")
    opcion = int(input("Ingresa un número válido de opción del menú: "))
    if opcion == 1:
        nombreEmpleado = ""
        while nombreEmpleado != "SALIR":
            nombreEmpleado = input("Ingresa el nombre del empleado (Si no deseas agregar más, oprime la tecla SALIR): ")
            if nombreEmpleado != "SALIR":
                empleados += nombreEmpleado + ","
    elif opcion == 2:
        print("Los empleados registrados son:", empleados)
    elif opcion == 3:
        nombreVisitante = ""
        while nombreVisitante != "SALIR":
            nombreVisitante = input("Ingresa el nombre del visitante (Si no deseas agregar más, digite SALIR): ")
            if nombreVisitante != "SALIR":
                visitantes += nombreVisitante + ","
    elif opcion == 4:
        print("Los visitantes registrados son:", visitantes)
    elif opcion == 0:
        bandera = False
        print("¡Hasta luego!")
    else:
        print("Por favor ingresa una opción válida")