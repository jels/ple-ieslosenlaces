# -*- coding: cp1252 -*-

"""
Escribe un programa cuadrilatero.py, que pide al usuario el valor
de los lados de un cuadrilátero y muestra en pantalla su perímetro
y su área.

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
print "El perimetro de un cuadrilátero de lados", lado1,  \
      "y", lado2, 'es', perim
print "El área de un cuadrilátero de lados", lado1, "y", lado2, 'es', area

# fin
raw_input("Pulsa intro para terminar")
