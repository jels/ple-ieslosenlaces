# -*- coding: cp1252 -*-
"""
Ejercicio que calcula la media de una suma de valores ...

El programa pide el número de entradas a sumar ...

"""

# Pedir número de entradas
veces = input("Introduzca número de datos a pedir: ")

# Inicializar variables (total)
total = 0  # Asigna valor a variable: inicializa  

# Pedir los números (range)
for x in range(veces):
    num = input('Introduzca valor: ')
    total = total + num  # Acumulamos valores

# Calcular la media y mostrar resultado
media = total / float(veces)

print "La media es", round(media, 2)

