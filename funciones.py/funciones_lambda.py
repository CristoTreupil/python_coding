numeros = [1,2,3,4,5,6,7,8,9,11,13,14,15,20]

# Creando una función lambda para multiplicar por dos   
multiplicar_por_dos = lambda x : x*2 # lambda (parametro) : expresión
# Lambda crea funciónes anonimas que retornan automaticamente
print(multiplicar_por_dos(5))

# Creando una función comun que diga si es par o no (Sin lambda)
def es_par(num):
    if (num%2==0):
        return True
# Usando filter como una función comun
numeros_pares = filter(es_par,numeros)

print(list(numeros_pares))

# Creando lo mismo pero con la función lambda
numeros_pares_lambda = filter(lambda numero:numero%2 == 0,numeros)
print(list(numeros_pares_lambda))