
# Propiedades de texto

# Tiene que ser un metodo pero no una funcion para que funcionen los comandos

# Ejemplo erroneo

cadena1 = "Hola soy mega"
cadena2 = "Bienvenido amigo"

#resultado = Upper(cadena1)
# Esto da error porque es una funcion la que se esta llamando y no un metodo

#Ejemplo Correcto

cadena1 = "Hola soy mega"
cadena2 = "Bienvenido amigo"

resultado = cadena1.upper()

print(resultado)
# Su formula es 
#     Dato . Metodo  (Parametro)


# Retonador de valores

# Buscar una cadena en otra cadena, si no existe coincidencia te devuelve -1

busqueda_find = cadena1.find("Hola")
print(busqueda_find)

# Buscar una cadena en otra cadena, pero si no coincide te tira un error/excepción y para el programa

busqueda_find = cadena1.index("a")

# Buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincide

contar_coincidencias = cadena1.count("a")

print(contar_coincidencias)

# Cuantos caracteres tiene una cadena

contar_caracteres = len(cadena1) # Es una función por esta razon se escribe de forma distinta

print(contar_caracteres)

# Remplaza un pedazo de la cadena por otra dada

cadena_nueva = cadena1.replace(" ", ",") # Se remplaza "la" por "lu"

print(cadena_nueva)

# Separar cadenas con la cadena que se le pase,  es la unica que devuelve una matriz/lista

cadena_separada = cadena_nueva.split(",")

print(cadena_separada) # Imprime la lista con sus separaciones
print(cadena_separada[1]) # Imprime la posicion 1 de la lista de cadena_separada
print(type(cadena_separada)) # que tipo de dato es "lista" porque fue actializada con .split