
edad = 17

if edad >= 18:
	print("Eres mayor de edad")
else:
	print("Eres menor de edad")
 
 
ingreso_mensual = 500000
gasto_mensual = 700
if ingreso_mensual > 10000: 
    if gasto_mensual < 7000: #Este es un if anidado a otro if mas grande, lo cual ayuda a filtrar o subpreguntar
        print("Estas bien en cualquier parte del mundo")
    else:
        print("Gastas demasiado")
elif ingreso_mensual > 1000: #si no tienes mas de 10.000 tu siguiente requisito es tener mas de 1000
    print("Estas bien en latinoamerica")
else: #si nisiquiera tienes mas de 1000 queda esta
    print("Eres pobre")