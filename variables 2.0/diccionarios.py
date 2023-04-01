# Creando diccionarios con dict()
diccionario = dict(nombre="Cristobal", apellido="Treupil")
print(diccionario)

# Las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["cris","pepe" ]):"jajajaja"}
print(diccionario)

# Creando diccionarios con fromkeys() valor por defecto: None
diccionario = dict.fromkeys(["nombre","apellido"]) # Diccionario None

# Creando diccionarios con fromkeys() cambiando el valor por defecto a "No se"
diccionario = dict.fromkeys(["nombre","apellido"],"No se") 


print(diccionario)