try:
    pregunta = int(input("Ingrese la cantidad de preguntas realizadas: "))
    correctas = int(input("Ingrese la cantidad de preguntas correctas: "))

    promedio = (correctas * 100) / pregunta
    if promedio < 50:
        print("Suspendido.")
    elif 50 <= promedio < 70:
        print("Aprobado.")
    elif 70 <= promedio < 90:
        print("Notable.")
    else:
        print("Sobresaliente.")
except ValueError:
    print("No es un valor válido.")