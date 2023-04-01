diccionario = {
    "nombre": "Cristobal",
    "apellido": "Treupil",
    "edad": 17
}

# Recorriendo diccionario con items para obtener la clave y el valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'La clave es: {key} y el valor es: {value}')