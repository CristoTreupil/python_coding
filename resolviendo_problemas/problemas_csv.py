# Cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv('resolviendo_problemas\\datos.csv')

# Convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)

# Mostrar el tipo de dato del primer elemento de la columna edad
print(type(df['edad'][0]))

# Reemplazando los datos Treupil por maestro
df['apellido'].replace('treupil','maestro',inplace=True)

print(df['apellido'])