def procesar_dato(peso, volumen):
    bandera = False
    if (peso < 2) and (volumen < 0.027):
        bandera = True
    return bandera

print(procesar_dato(1, 0.01))