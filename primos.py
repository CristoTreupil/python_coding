def es_primo(num):
    # Verificar si el número entregado no pueda dividirse por ningun número entre 2 y por si mismo -1
    for i in range(2,num-1):
        # Si es divisible por alguno retornamos False y termina el bucle
        if num%i==0: return 'No es primo'
        # Si termina el bucle, significa que no fue divisible y entonces es primo
    return 'Es primo'

num = int(input('Ingresa número: '))
resultado = es_primo(num)
print(resultado)