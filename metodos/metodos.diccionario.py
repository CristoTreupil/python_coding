diccionario = {
    "nombre" : "Cristobal",
    "apellido" : "Treupil",
    "edad" : 17
}

# Devuelve las claves nombre, apellido, edad (Sirve para iterar)
claves = diccionario.keys()

# Obtiene un elemento con get() si no encuentra nada el programa continua
valor_de_edad = diccionario.get("edad")

#  diccionario.clear() # Elimina todo el diccionario

# Elimina un elemento del diccionario
diccionario.pop("edad") # Si no coincide, lanza excepción

# Obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()
# Iterar es igual a recorrer el elemento

print(diccionario_iterable)