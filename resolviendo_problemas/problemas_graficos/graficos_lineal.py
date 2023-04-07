import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('resolviendo_problemas\\problemas_graficos\\pedos.csv')

sns.lineplot(x='fecha',y='pedos', data=df)

# Creando un punto en el lugar más alto
plt.plot('01-11',55,'o')

plt.show()