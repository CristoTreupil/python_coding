# Abriendo el archivo con with open
with open('archivos\\texto_cristobal.txt', encoding = 'UTF-8') as archivo: # la ruta = a la variable "archivo"

    # leemos el archivo
    contenido = archivo.read()

    # Mostramos el archivo
    print(contenido)
    
# No es necesario cerrarlo al usar with open