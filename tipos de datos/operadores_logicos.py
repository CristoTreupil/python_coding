#AND
#Las dos condiciones o valores tienen que ser True,  si una es False da False si o si
Resultado1 = True & True #Devolver True 
Resultado2 = False & True #Devolver Falso
Resultado3 = True & False #Devolver Falso
Resultado4 = False & False #Devolver Falso


#OR
#Lo contrario a AND osea que si los valores no son iguales es True,  pero si ambos son False es falso
Resultado5 = True | True #Devolver True
Resultado6 = False | True #Devolver True
Resultado7 = True | False #Devolver True
Resultado8 = False | False #Devolver Falso


#NOT
#Invierte valores,  si era True ahora es False
Resultado9 = not True #Devolver Falso
Resultado10 = not False #Devolver True

print(Resultado1)