def media(nota1, nota2):
    return (nota1 + nota2) / 2

def validar(nota):
    msg = ('Reprueba con ' + str(nota))
    if nota >= 6:
        msg = ('Aprueba con ' + str(nota))
    return msg

# notafinal = media(6, 4)
# aprueba = validar(notafinal)
# print(aprueba)
# aprueba = validar(notafinal:=media(6, 8))
# print(aprueba)

fSalir = False
while fSalir == False:
    opcion = int(input('1. Calcular Nota\n0.Salir\n'))
    print('============================')
    if opcion == 0:
        print('Saliendo.')
        fSalir = True
    if opcion == 1:
        n1 = float(input('Nota 1:\n'))
        n2 = float(input('Nota 2:\n'))
        aprueba = validar(notafinal:=media(n1, n2))
        print(aprueba)
        print('============================')
        