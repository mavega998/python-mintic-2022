saldo = 0
bandera = True
while bandera:
    try:
        valor = int(input("Ingresar valor\n(Para salir ingrese 0)\n")) 
        if valor == 0:
            bandera = False
            descuento = 0
            if saldo > 1000:
                descuento = 10
                saldo = saldo - (saldo * 0.1)
            print("Saldo a pagar:", int(saldo), "pesos. Tuvo un descuento del", descuento, "%.")
            print("Saliendo...")
        elif valor < 0:
            print("No debe ser valor negativo.")
        else:
            saldo += valor
    except ValueError:
        print("Valor no válido.")