otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_prom = 4
otros_cursos_crudo = 5

curso_actual = 1.5
curso_actual_crudo = 3.5

# Diferencia de duracion
diferencia_min = 100 - curso_actual / otros_cursos_min *100
diferencia_max = 100 - curso_actual / otros_cursos_max *100
diferencia_prom = 100 - curso_actual / otros_cursos_prom *100

# Tiempo vacio promedio
tiempo_vacio_promedio = 100 - otros_cursos_prom / otros_cursos_crudo *100

tiempo_vacio_dalto = 100 - curso_actual / curso_actual_crudo *100
print("----------------------------------------")

# Diferencias entre los cursos (Ejercicio A)
print(f'El curso de dalto dura un {diferencia_min}% menos que el más rapido de los otros')
print(f'El curso de dalto dura un {round(diferencia_max,2)}% menos que el más largo de los otros')
print(f'El curso de dalto dura un {diferencia_prom}% menos que el promedio de los otros')

print("----------------------------------------")

# Porcentaje vacio de cursos (Ejercicio B)
print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Curso de dalto promedio elimina un {round(tiempo_vacio_dalto,2)}% de tiempo vacio')

print("----------------------------------------")

# Mostrar diferencias de 10 horas (Ejercicio C)
print (f'Ver 10 horas de este curso equivale a {otros_cursos_prom *100 // curso_actual / 10} horas de otros cursos')
print (f'Ver 10 horas de otros cursos equivale a {curso_actual *100 // otros_cursos_prom / 10} horas de este curso')

print("----------------------------------------")