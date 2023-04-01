# Crear un conjunto con set(iterable)
conjunto = set(["dato1","dato2"])

# Meter un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"}


# Teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

# El metodo da el resultado si el (conjunto2) es subconjunto de (conjunto1)
resultado_subconjunto_conjunto2 = conjunto2.issubset(conjunto1) # True (conjunto2) es subconjunto de (conjunto1)
resultado_subconjunto_conjunto1 = conjunto1.issubset(conjunto2) # False (conjunto1) no es subconjunto de (conjunto2)
resultado_subconjunto_alternativo = conjunto2 <= conjunto1 # True (conjunto2) es subconjunto de (conjunto1)

# El metodo da el resultado si el (canjunto2) es superconjunto de (conjunto1)
resultado_superconjunto_conjunto2 = conjunto2.issuperset(conjunto1) # False (conjunto2) no es superconjunto de (conjunto1)
resultsdo_superconjunto_conjunto1 = conjunto1.issuperset(conjunto2) # True (conjunto1) es superconjunto de (conjunto2)
resultado_superconjunto_alternativo = conjunto2 > conjunto1 # False (conjunto2) no es superconjunto de (conjunto1)

print("-----------------------")
print("conjunto2 es subconjunto de conjunto1? ", resultado_subconjunto_conjunto2)
print("conjunto1 es subconjunto de conjunto2? ", resultado_subconjunto_conjunto1)
print("Verificación alternativa = ", resultado_subconjunto_alternativo)
print("-----------------------")
print("conjunto2 es superconjunto de conjunto1? ", resultado_superconjunto_conjunto2)
print("conjunto1 es superconjunto de conjunto2? ", resultsdo_superconjunto_conjunto1)
print("Verificación alternativa = ", resultado_superconjunto_alternativo)
print("-----------------------")
