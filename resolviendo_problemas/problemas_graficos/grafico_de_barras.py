import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('resolviendo_problemas\\problemas_graficos\\ingresos.csv')

# Creando Grafico
sns.barplot(x='fuente',y='ingresos',data=df)

# Obteniendo el total de ingresos
total_ingresos = df['ingresos'].sum()

# Mostrando el total
print(f'El total de ingresos es: ${total_ingresos} USD')

# Mostrando el grafico
plt.show()
