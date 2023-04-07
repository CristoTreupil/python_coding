archivo = open('archivos\\texto_cristobal.txt',encoding = 'UTF-8')
# Leer archivo completo
# archivo = archivo_sin_leer.read()

# Leer linea especifica
# lineas = archivo_sin_leer.readlines()

# Leer solo una línea
linea = archivo.readline()

# Cerrar el archivo
archivo.close()

print(linea)