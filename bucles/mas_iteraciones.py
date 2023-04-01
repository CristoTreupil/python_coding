frutas = ["manzana","pera","naranja","durazno","palta","banana"]

# Evitar que se coma una palta con la secuencia continue
for fruta in frutas:
    if fruta == "palta":
        continue # Se salta la siguiente vuelta y no aparece
    print(f'Me voy a comer una {fruta}')
    
print('----------------')

# Evitar que el bucle siga ejecutandose
for fruta in frutas:
    if fruta == "durazno":
        break # Termina el bucle aquí y no se come el durazno
    print(f'Me voy a comer una {fruta}')
    
print('Bucle terminado!')

print('----------------')

for fruta in frutas:
    print(f'Me voy a comer una {fruta}')
    if fruta == "durazno":
        break # Termina el bucle aquí y se come el durazno

# Recorrer/iterar cadena de texto
cadena = "Hola Cristobal"

for letra in cadena:
    print(letra)

# For en una sola linea de codigo
numeros = [2,8,19,57]
numeros_duplicados = [x*2 for x in numeros] # variable x es igual a la multiplicación (por 2) y esa se aplica al (in) en (numeros)
print(numeros_duplicados)