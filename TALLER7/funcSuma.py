def suma(a, b):
    return a + b

try:
    print("Vamos a sumar dos números")
    num1 = int(input("Ingrese número: "))
    num2 = int(input("Ingrese número: "))
    resultado = suma(num1, num2)
    print(f"Resultado: {num1} + {num2} = {resultado}")
except ValueError:
    print("Valor no válido.")
