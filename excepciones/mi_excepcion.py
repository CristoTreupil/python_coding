# Creando mi propia excepción personalizada
class Miexcepcion(Exception):
    def __init__(self,err):
        print(f'Cometiste el siguiente error: {err}')


# Lanzando mi propia excepción
#raise Miexcepcion('Termino amigo...')

# Manejandola
try:
    raise Miexcepcion('JAJAJAJ, persona torpe') # raise palabra clave para lanzar excepciones
except:
    print('Como vas a cometer ese error?')    
