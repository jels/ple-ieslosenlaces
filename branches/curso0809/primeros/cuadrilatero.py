# -*- coding: cp1252 -*-

"""
Escribe un programa cuadrilatero.py, que pide al usuario el valor
de los lados de un cuadril�tero y muestra en pantalla su per�metro
y su �rea.

AUTOR
VERSION
"""

# pedir datos
lado1 = input("Introduce el primer lado: ")
lado2 = input("Introduce el segundo lado: ")

# calcular resultado
perim = lado1 * 2 + lado2 * 2
area = lado1 * lado2


# mostrar el resultado
print "El perimetro de un cuadril�tero de lados", lado1,  \
      "y", lado2, 'es', perim
print "El �rea de un cuadril�tero de lados", lado1, "y", lado2, 'es', area

# fin
raw_input("Pulsa intro para terminar")
