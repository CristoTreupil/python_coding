animales = ["Conejo","Loro","Gato","Perro"]
numeros = [72,27,94,12]

# Se ejecutara cuantas veces necesite para terminar y de esta forma se itera la lista
for animal in animales: # (animal) sera una variable que solamente para ser utilizada dentro de este bloque de codigo
    print(f'La variable animal es igual a: {animal}')
    
for numero in numeros:
    resultado = numero * 10
    print(resultado)
    
# Iterar dos listas al mismo tiempo con zip()
for numero,animal in zip(animales,numeros): # Las listas tienes que tener la misma cantidad de elementos
    print(f'Recorriendo lista 1: {numero}')
    print(f'Recorriendo lista 2: {animal}')
    
for num in range(5,10): # Con dos parametros se determina inicio y final, con un parametro se determina desde el 0 hasta ese numero
    print(num)
    
print("------------------------")
    
# Forma correcta de recorrer una lista con su indice y obtener el indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'El indice: {indice} es el valor: {valor}')
    
print("-------------------")
    
# Forma de desempaquetar la tupla directamente en el for, forma mas practica y elegante
for num,i in enumerate(numeros):
    print(num)

# Utilizando el for/else
for numero in numeros:
    print(f'ejecutando el ultimo bucle, valor actual: {numero}')

else:
    print('El bucle termino') # Se ejecute siempre al final del bucle haya o no datos a no ser que haya un break
    
# Todo lo anterior funciona exactamente igual para tuplas y un poco diferente para conjuntos