import re

# La cadena en la que se buscaran los patrones
text = "La fecha es 23/06/2021 y el teléfono es +1-555-555-5555"

# El patron a buscar
pattern = r'\d{2}/\d{2}/\d{4}' # Encontrar que hayan 2 numeros y una /, encontrar que hayan 2 numeros y una /, encontrar que hayan 4 numeros

# El texto con el que se reemplazara el patrón
replacement = 'Fecha oculta'

# Reemplazar todas las apariciones del patrón en la cadena de texto
new_text = re.sub(pattern, replacement, text) # re.sub (Substituir algo por otra cosa)

# Imprimir el resultado
print(f'Texto modificado es: {new_text}')
