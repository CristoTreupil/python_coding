# Creando una función que nos devuelva los numeros primos
# Entre el 0 y el argumento que pasamos

# Crear función que verifique si el número ingresado es primo o no
def es_primo(num):
    # Verificar si el número entregado no pueda dividirse por ningun número entre 2 y por si mismo -1
    for i in range(2,num-1):
        # Si es divisible por alguno retornamos False y termina el bucle
        if num%i==0: return False
        # Si termina el bucle, significa que no fue divisible y entonces es primo
    return True

# Crear función que retorne lista con números primos
def primos_hasta(num):
    primos = []
    for i in range(2,num+1):
        # Verificamos si el valor es primo
        resultado = es_primo(i)
        # Si es primo se agrega a la lista
        if resultado == True: primos.append(i) # Ingresar números primos a la lista
    # Devolvemos la lista con sus valores nuevos
    return primos
            

num = int(input('Ingresa número: '))
resultado = primos_hasta(num)
print(resultado)




# Otra forma
primos_hasta2 = lambda num: list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)), range(2, num)))

print(primos_hasta2(15))
# Muestra [2, 3, 5, 7, 11, 13]