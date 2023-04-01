# Creando una función de 3 parametros
def frase(nombre,apellido,adjetivo): # nombre,apellido,adjetivo son parametros posicionales
    return f'Hola {nombre} {apellido} eres muy {adjetivo}'

frase_resultante = frase("Cristobal","Treupil","Master")
# Utilizando keyword arguments
frase_resultante = frase(adjetivo="Master",nombre="Cristobal",apellido="Treupil") # No cambia nada, pero los parametros cambian de lugar, son parametros de palabra clave

print(frase_resultante)

# Creando la misma función con un parametro opcional y un valor por defecto
def frase(nombre,apellido,adjetivo='tonto'): # Significa que adjetivo siempre sera = a 'tonto' porque viene definido
    return f'Hola {nombre} {apellido} eres muy {adjetivo}'

frase_resultante = frase("Cristobal","Treupil"'inteligente') # Reescribe el parametro y lo actualiza eso hace que se defina
print(frase_resultante)