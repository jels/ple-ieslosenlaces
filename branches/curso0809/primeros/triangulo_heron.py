# -*- coding: cp1252 -*-
"""
Escribe un programa area_triangulo.py que calcule el �rea de un tri�ngulo,
conocida la longitud de sus tres lados. Utiliza la f�rmula de Her�n.
AUTOR: Jes�s Mart�nez
"""

#Se importa la operaci�n de ra�z cuadrada
from math import sqrt

#Se piden los datos de entrada
ladoA = input('Introduce el valor del primer lado del tri�ngulo: ')
ladoB = input('Introduce el valor del segundo lado del tri�ngulo: ')
ladoC = input('Introduce el valor del tercer lado del tri�ngulo: ')

#Se realizan las operaciones oportunas
semiP = (ladoA + ladoB + ladoC)/2
area = sqrt(semiP * (semiP - ladoA) * (semiP - ladoB) * (semiP - ladoC))

#Se muestran los resultados por pantalla
print 'El �rea del tri�ngulo de lados', ladoA, ',', ladoB, ',', ladoC, 'es', area

#Fin
raw_input('Pulse Intro para terminar...')
