# -*- coding: cp1252 -*-


"""
Escribe un programa circulo.py, que pide al usuario el lado de
un círculo y muestra en pantalla la circunferencia y el área del círculo.
AUTOR
VERSION
"""

from math import pi

# pedir datos
radio = input("Introduce el radio: ")

# calcular resultado
circunf = 2 * pi * radio
area = pi * radio ** 2


# mostrar el resultado
print "La circunferencia de un círculo de radio", radio, 'es', round(circunf, 2)
print "El área de un círculo de radio", radio, 'es', round(area, 2)

# fin
raw_input("Pulsa intro para terminar")
