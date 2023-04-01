k = 0
s = 0

numero_ingresado = input('Ingresar número: ')

n = int(numero_ingresado)

while k <= 5:
    s += n
    n -= 4
    k += 1
else:
    print(f'el valor s es: {s} y el valor n es: {n} k es {k}')
