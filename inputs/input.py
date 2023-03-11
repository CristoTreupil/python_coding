# Pedirle un dato al usuario
nombre = input("Dame tu nombre: ")

print(f"Bienvenido {nombre}") # Se puede concatenar
# Input siempre devuelve texto (String)



numero = input("Dame un numero: ")
# Convertir texto a numero entero
resultado_entero = int(numero) * 2

# Convertir texto a numero flotante
resultado_flotante = float(numero) *2

print(resultado_entero)
print(resultado_flotante)