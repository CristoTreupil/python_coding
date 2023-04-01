# Creando una función simple
def saludar(): # Definir nombre de la variable y su parametro correspondiente
    print('Hola Cristobal como estas??')

# Ejecutando una función simple    
saludar()

# Crear una función con parametro = (Una variable que existe dentro de una función)
def saludo(nombre,sexo):
    sexo = sexo.lower() # Convierte todo a minuscula
    if (sexo == "mujer"):
        adjetivo = "maestra"
    elif (sexo == "hombre"):
        adjetivo = "maestro"
    else:
         adjetivo = 'ser humano'
    print(f'Hola {nombre} que me cuentas {adjetivo}?')

saludo('Cristobal','Mujer')

# Crear una función que nos retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghij" # Cadena de valores (Caracteres)
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num -5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
    return contraseña,num # Esto es una tupla # Sirve para retornar valores que la variable nos da
    
# Desempaquetando la función
resultado_contraseña,numero_usado = crear_contraseña_random(98)

# Mostrando los resultados obtenidos y los datos utilizados para obtenerlo 
print(f'Tu contraseña nueva es: {resultado_contraseña} y el número usado fue {numero_usado}')

