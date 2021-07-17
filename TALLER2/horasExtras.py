horas = int(input("Ingrese horas trabajadas: "))
precioHora = 20000

print("Su dinero es:")
if horas <= 40:
    print(horas * precioHora)
elif horas <= 48:
    extra = horas - 40
    base = 40 * precioHora
    print(base + (extra * (precioHora * 2)))
else:
    extra = horas - 48
    base1 = 40 * precioHora
    base2 = 8 * (precioHora * 2)
    print(base1 + base2 + (extra * (precioHora * 3)))