lista = list(["hola", "amigo", 34, True])

# Devuelva la cantidad de elementos de la lista
cantidad_elementos = len(lista)

# Agregar un elemento a la lista
lista.append("JAJAJA")

# Agrega un elemento a la lista, pero en un indice especifico
lista.insert(2,"TOMA AMIGOO")

# Agrega mas de un elemento a la lista
lista.extend([False, 2030]) # Tiene que ir con corchete porque le estamos pasando una lista

# Eliminar un elemento de la lista
# Eliminar ultimo elemento de la lista -1 y -2 eliminar anteultimo
lista.pop(0)

# Remover elemento de la lista por su valor
lista.remove("TOMA AMIGOO") # Con lo que esta dentro del elemento de la lista
# Si no encuentra nada salta una excepcion y para el programa

# Elimina todos los elementos de la lista
# lista.clear()

# Ordena los elementos de forma ascendente, pero no pasa cadenas de texto
listas = ([24, 78, 16, 2, False, True]) # Los ordena por orden numerico
listas.sort() # lista.sort(reverse=True)  Hace que el orden se de vuelta y se impriman alrevez

# Invertir elementos de una lista
listas.reverse() # Invierte cualquier lista aunque tenga cadenas de texto

print(lista)
print(listas)