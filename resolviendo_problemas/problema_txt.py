# 2 listas , una con nombres otra con apellidos
nombres = ['Cristobal','Raul','Paulina','Fabian']
apellidos = ['Treupil','Castillo','Yañez','Cuevas']

# Registrar esta información en un TXT de forma óptima

with open('resolviendo_problemas\\nombres_y_apellidos.txt','w',encoding = 'UTF-8') as arch:
    arch.writelines('Los datos son:\n\n')
    # Poniendo el for dentro de una lista para simplificarlo
    [arch.writelines(f'Nombre: {n}\nApellido: {a}\n----------\n') for n,a in zip(nombres,apellidos)]
    