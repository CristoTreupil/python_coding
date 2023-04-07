# Si A es menor a B se suman los números entre ellos y si no es menor a b muestra 0
a = int(input('Ingresar primer número: '))
b = int(input('Ingresar segundo número: '))
s = 0
c = a + 1
# a es menor a b? te mete a bucle
if a < b:
    # contador es menor a el número B? si es asi aplicar la aritmetica 
    while c < b:
        s += c
        c += 1
    # Si C no es menor a B mostrar la suma
    print(s)
        
# Si A no es menor a B entonces mostrar 0 (la suma la cual queda en cero al saltar todo lo anterior)
else:
    print(s)