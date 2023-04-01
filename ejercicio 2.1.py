# Falto el profesor y los alumnos haran la clase

# Pedir el nombre y edad de los alumnos que vinieron hoy clase
# Función para obtener el asistente y el profesor segun la edad.
def obtener_compañeros(cantidad_de_compañeros):
    # Creando la lista de compañeros
    compañeros = []

    # Ejecutando un For para pedir información de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input('Ingrese el nombre del compañero: ')
        edad = int(input('Ingrese la edad del compañero: '))
        compañero = (nombre,edad)

        # Agregando la información a la lista
        compañeros.append(compañero)

    # Ordenandolos de menor a mayor según su edad    
    compañeros.sort(key=lambda x:x[1])

    # Compañero[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre
    # Para definir el asistente y al profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]

    # Retornamos una tupla
    return asistente,profesor

# Desempaquetamos lo que nos retorne la función
asistente,profesor = obtener_compañeros(5)

print(f'El asistente es: {asistente}')
print(f'El profesor es: {profesor}')