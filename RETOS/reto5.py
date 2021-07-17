diccionario = {
    'enero': [4,3,4],
    'febrero': [4,5],
    'marzo':[3,1],
    'abril':[3]
}

for i in range(1,5):
    aportes = input()
    if i == 1:
        diccionario['enero'] = [aportes]
    elif i == 2:
        diccionario['febrero'] = [aportes]
    elif i == 3:
        diccionario['marzo'] = [aportes]
    elif i == 4:
        diccionario['abril'] = [aportes]

print(diccionario.values())