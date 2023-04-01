import pandas as pd
df = pd.read_csv('archivos\\datos.csv') # DF = "Data Frame" son estructura de datos como hojas de calculo
df2 = pd.read_csv('archivos\\datos.csv')
# Se divide entre filas y columnas

# Obteniendo los datos de la columna "nombre"
nombres = df['nombre']

cadena = "0123456789"
# print(cadena[0:7]) # Slicing

# Ordenando el dataframe por la edad
df_orden_ascendente = df.sort_values('edad')

# Ordenandolo de forma descendente
df_orden_descendente = df.sort_values('edad',ascending = False)

# Concatenando los dos DataFrames
df_concatenado = pd.concat([df,df2]) # Pide una lista con todo lo que queremos concatenar

# Accediendo a la primeras 3 filas con head()
primeras_filas = df.head(3)

# Accediendo a las ultimas 3 filas con tail()
ultimas_filas = df.tail(3)

# Accediendo a la cantidad de filas y columnas con shape
filas_totales,columnas_totales = df.shape 

# Obteniendo data estadistica del DataFrame: (Esto es más utilizado en analisis de datos)
df_info = df.describe()

# Accediendo a un elemento especifico del DataFrame con loc
elemento_especifico_loc = df.loc[2,'edad']

# Accediendo a un elemento especifico del DataFrame con iloc
elemento_especifico_iloc = df.iloc[2,2]

# Accediendo a todas las filas de una columna
apellidos = df.iloc[:,1]

# Accediendo a las filas mayores que 30
mayor_que_30 = df.loc[df['edad']>30,:]

print(mayor_que_30)
