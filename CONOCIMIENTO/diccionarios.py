productos = [
    {"sku": 1, "fecha_expiracion": "hoy", "precio": 207.909, "descuento": 0},
    {"sku": 2, "fecha_expiracion": "", "precio": 238.392, "descuento": 4},
    {"sku": 3, "fecha_expiracion": "", "precio": 38.482, "descuento": 13},
    {"sku": 4, "fecha_expiracion": "", "precio": 222.696, "descuento": 28}
]

i = 0
for producto in productos:
    producto['sku'] = f'{i}'
    i += 1

print(productos)