# -*- coding: cp1252 -*-
"""
Escribe un programa area_triangulo.py que calcule el área de un triángulo,
conocida la longitud de sus tres lados. Utiliza la fórmula de Herón.
AUTOR: Jesús Martínez
"""

#Se importa la operación de raíz cuadrada
from math import sqrt

#Se piden los datos de entrada
ladoA = input('Introduce el valor del primer lado del triángulo: ')
ladoB = input('Introduce el valor del segundo lado del triángulo: ')
ladoC = input('Introduce el valor del tercer lado del triángulo: ')

#Se realizan las operaciones oportunas
semiP = (ladoA + ladoB + ladoC)/2
area = sqrt(semiP * (semiP - ladoA) * (semiP - ladoB) * (semiP - ladoC))

#Se muestran los resultados por pantalla
print 'El área del triángulo de lados', ladoA, ',', ladoB, ',', ladoC, 'es', area

#Fin
raw_input('Pulse Intro para terminar...')
