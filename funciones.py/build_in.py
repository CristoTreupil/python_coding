numeros = [5,13,6,4,78]

# Encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

# Encontrando el numero menor de una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

# Redondeando a 6 decimales
numero = round(21.4345,2) # , y cantidad de decimales
print(numero)

# Retornar False -> 0, vacio, False, ninguno \ True -> Si es distinto a 0, cadena de texto, datos no vacios
resultado_bool = bool()
print(resultado_bool)

# Retorna True, si todos los valores son verdaderos
resultado_all = all([0,"true",[344,23]]) # Comprueba lo que esta adentro de un iterable
print(resultado_all)

# Suma todos los valores de un iterable
suma_total = sum(numeros)
print(suma_total)