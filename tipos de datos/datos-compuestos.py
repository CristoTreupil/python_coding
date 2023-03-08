#Las listas se pueden modificar
lista = ["Cristobal treupil", "Xwmega", True, 1.70]
#numero de elementos Cristobal= elemento 1  , 1.70 = elemento 4
#lista = [0, 1, 2, 3] numero de datos
print(lista[3])
#1.7


#esta no se puede modificar
tupla = ("Cristobal treupil", "Xwmega", True, 1.70)
print(tupla[2])
#True

#Son elementos desordenados que pueden intercambiar lugares, pero no modificarse nuevos y no se repiten valores
conjunto = {"Cristobal treupil", "Xwmega", True, 1.70}
print(conjunto)
#{1.7, 'Cristobal treupil', 'Xwmega', True}

#Creando un diccionario (dict)
diccionario = {
    'Nombre' : "Cristobal Treupil", #key : value
    'Canal' : "Xwmega", #key : value
    'Esta emocionado' : True, #key : value
    'Altura' : 1.70 #key : value
}
# print(diccionario[key])
print(diccionario['Nombre'])
#Cristobal Treupil
