import re

texto = '''Hola amigo, como estas? es la 1. ra
Esta es la 2da linea de texto
y esta es la final total con la 3ra'''

# Haciendo busquedas simples

# Search encuentra coincidencias y las devuelve
resultado = re.search('Hola', texto) # Buscar "hola" en la cadena de texto llamada "texto"

# Mostrar todas las coincidencias en una lista
resultado_findall = re.findall('esta', texto,flags=re.IGNORECASE) # re.IGNORECASE para ignorar las mayusculas y minusculas

#print(resultado_findall)

# \d --> busca digitos númericos del 0 - 9
resultado_d = re.findall(r'\d',texto) # r'' Es para usar expreciones regulares

# \D --> busca TODO MENOS digitos númericos del 0 - 9
resultado_D = re.findall(r'\D',texto)

# \w --> busca caracteres alfanumericos [a-z A-Z 0-9 _]
resultado_w = re.findall(r'\w',texto)

# \W --> busca TODO MENOS caracteres alfanumericos [a-z A-Z 0-9 _]
resultado_W = re.findall(r'\W',texto)

# \s --> busca espacios en blanco -> espacios, tabs, saltos de linea
resultado_s = re.findall(r'\s',texto)

# \S --> busca TODO MENOS espacios en blanco -> espacios, tabs, saltos de linea
resultado_S = re.findall(r'\S',texto)

# . --> busca TODO MENOS saltos en linea
resultado_punto = re.findall(r'.',texto)

# \n --> Busca saltos en linea
resultado_n = re.findall(r'\n',texto)

# \ --> Cancelar caracteres especiales ?,-,()
resultado_barra = re.findall(r'\?',texto)

# Armando una cadena que busque un número, seguido de un punto y un espacio
resultado = re.findall(r'\d\.\s',texto) # Encuentra una cosa exacta y especifica como (1. )

# ^ --> Busca el comienzo de una linea
resultado_comienzo_de_linea = re.findall(r'^Esta',texto,flags=re.M)

# $ --> Busca el final de la linea
resultado_final_de_linea = re.findall(r'ra$',texto)

# | --> Busca una cosa o la otra
resultado_linea = re.findall(r'\d{2,4}|Hola',texto)

print(resultado_linea)
