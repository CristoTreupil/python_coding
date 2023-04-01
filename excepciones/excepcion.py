def suma_total():
    # iniciando bucle
    while True:
        a = (input('Ingresar 1er num: '))
        b = (input('Ingresar 2do num: '))
        try: # Ve si lanza excepción
            # Intentar convertirlos a enteros y sumarlos
            resultado = int(a) + int(b)
        # Si lanza excepción, pide que reingrese los datos
        except Exception as e: # Si try lanza excepción tira lo siguiente
            print('Te pedi un número')
            print(f'ERROR: {e}')
            #print(f'ERROR: {type(e).__name__}') # da (ERROR: ValueError)
        # Si todo salio bien terminar el bucle
        else:
            break
        finally: # Muestra el finally lance o no excepción
            print('Manejo de excepción finalizado')
    return resultado

print(suma_total())