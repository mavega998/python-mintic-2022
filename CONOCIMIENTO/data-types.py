## int
x = 1
print(x, type(x))

## float
y = 1.0
print(y, type(y))

## string
z = 'hola'
print(z, type(z))

## bool
a = True
print(a, type(a))

## list
b = [1,2,3,4,5]
print(b, type(b))

## tuple
c = (1,2,3,4,5, (6,7,8,9))
print(c, type(c))

## dictionary
d = {
    "name": "Pedro",
    "lname": "Pérez",
    "birth": "01-01-1978",
    "gender": "male"
}
print(d, type(d))
print(d.keys())
print(d.values())
print(d.items())