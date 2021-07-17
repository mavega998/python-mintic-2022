def conteoHuevos(cantAAA, cantAA, cantA, cantBC):
    print(f'tipo_huevos:A numero_huevos: {cantA} numero_bandejas: {cantBandejas(cantA, 30)}')
    print(f'tipo_huevos:AA numero_huevos: {cantAA} numero_bandejas: {cantBandejas(cantAA, 24)}')
    print(f'tipo_huevos:AAA numero_huevos: {cantAAA} numero_bandejas: {cantBandejas(cantAAA, 12)}')
    print(f'tipo_huevos:BC numero_huevos: {cantBC} numero_bandejas: {cantBandejas(cantBC, 30)}')

def cantBandejas(cantHuevos, tamanioBandeja):
    cantBandejas = cantHuevos // tamanioBandeja
    respuesta = 'None'
    if (cantBandejas > 0):
        respuesta = str(cantBandejas)
    return respuesta

cantidadIngresar = float(input())
contadorHuevosA = 0
contadorHuevosAA = 0
contadorHuevosAAA = 0
contadorHuevosBC = 0
i = 0
while (i < cantidadIngresar):
    tamanio = float(input())
    if tamanio > 67:
        contadorHuevosAAA += 1
    elif tamanio >= 60 and tamanio < 67:
        contadorHuevosAA += 1
    elif tamanio >= 53 and tamanio < 60:
        contadorHuevosA += 1
    elif tamanio >= 46 and tamanio < 53:
        contadorHuevosBC += 1
    else:
        contadorHuevosBC += 1
    i += 1

conteoHuevos(contadorHuevosAAA, contadorHuevosAA, contadorHuevosA, contadorHuevosBC)
