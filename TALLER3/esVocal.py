cadena = input("Ingrese un caracter: ")

def isVowel(letter):
    return letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'

if 0 < len(cadena) > 1:
    print("No se puede procesar el dato.")
elif isVowel(cadena):
    print("Es vocal.")
elif cadena.isnumeric():
    print("Es número.")
elif cadena.isalpha():
    print("Es letra.")
else:
    print("Es símbolo.")