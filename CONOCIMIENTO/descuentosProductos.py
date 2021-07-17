# productos = [
#     {"sku": 1, "fecha_expiracion": "", "precio": 376.443, "descuento": 0},
#     {"sku": 2, "fecha_expiracion": "hoy", "precio": 84.945, "descuento": 31},
#     {"sku": 3, "fecha_expiracion": "", "precio": 941.135, "descuento": 15},
#     {"sku": 4, "fecha_expiracion": "hoy", "precio": 40.244, "descuento": 20},
#     {"sku": 5, "fecha_expiracion": "hoy", "precio": 796.153, "descuento": 21},
#     {"sku": 6, "fecha_expiracion": "hoy", "precio": 308.358, "descuento": 0},
#     {"sku": 7, "fecha_expiracion": "hoy", "precio": 457.561, "descuento": 20},
#     {"sku": 8, "fecha_expiracion": "", "precio": 322.529, "descuento": 7}, 
#     {"sku": 9, "fecha_expiracion": "hoy", "precio": 837.608, "descuento": 0}
# ]

productos = [
    {"sku": 1, "fecha_expiracion": "hoy", "precio": 207.909, "descuento": 0},
    {"sku": 2, "fecha_expiracion": "", "precio": 238.392, "descuento": 4},
    {"sku": 3, "fecha_expiracion": "", "precio": 38.482, "descuento": 13},
    {"sku": 4, "fecha_expiracion": "", "precio": 222.696, "descuento": 28}
]

# import json
# productos = json.loads(input())
resultado = 0

for producto in productos:
    if (producto['fecha_expiracion'] == 'hoy'):
         producto['precio'] -= ((producto['precio'] * 20) / 100)
    resultado += producto['precio'] - ((producto['precio'] * producto['descuento']) / 100)
    resultado = round(resultado, 2)

print(resultado)