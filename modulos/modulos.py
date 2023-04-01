# Importar modulo y asignandole el nombre "m_saludar"
import modulo_saludar as m_saludar

# Desde el modulo, importamos dos funciones
from modulo_saludar import saludar,saludo_loco as saludar_como_coscu
# saludo = modulo_saludar.saludo("cris")

# Creamos las variables con los saludos
saludo = saludar('Xwmega')
saludo_raro = saludar_como_coscu('Cris')
print(saludo)
print(saludo_raro)

# Accedemos al nombre de este modulo
print(__name__)
# Accedemos al nombre del modulo
# print(m_saludar.__name__)