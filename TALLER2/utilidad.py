meses = int(input("Ingrese tiempo (meses): "))
anios = meses / 12

print("Utilidad")
if anios < 1:
    print("5%")
elif anios >= 1 and anios < 2:
    print("7%")
elif anios >= 2 and anios < 5:
    print("10%")
elif anios >= 5 and anios < 10:
    print("15%")
else:
    print("20%")
