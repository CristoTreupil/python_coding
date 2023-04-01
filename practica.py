# Variables
numero = int(input('Ingresar número: '))
contador = 0
suma = 1

while suma < numero:
    print(suma)
    suma = suma + contador # 1 + 0 = 1(#1) - 1 + 1 = 2 (#2) - 2 + 1 = 3
    contador = suma - contador # 0 + 1 = 1 (#!) - 2 - 1 = 1 (#2) - 
    
print('fin')
