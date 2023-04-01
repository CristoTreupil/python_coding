# Utilizando el operador * como argumento (*args)
def suma(nombre,*numeros): # El * tiene que ser el ultimo parametro que agregemos, o si no no se podra poner mas parametros
      return f'{nombre}, la suma de los números es: {sum(numeros)}'
     
resultado = suma("Cristobal",4,5,6,7)
print(resultado)

# Forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([5,3,9,10,20,3])

print(f'La suma total es: {resultado2}')