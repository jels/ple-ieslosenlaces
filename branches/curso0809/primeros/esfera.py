# -*- coding: cp1252 -*-



'''
Escribe un programa esfera.py
que calcule el volumen y la superficie de una esfera a partir del radio,
que se pide al usuario.
Aquí tienes las fórmulas necesarias:
http://es.wikipedia.org/wiki/Esfera#.C3.81rea_y_volumen

AUTOR: PABLO MARTIN
VERSION: 1.0
'''

#Importamos de math el valor de pi
from math import pi

#Presentacion del programa
print 'Hola, este programa calculara el volumen y la superficie de una esfera \
a partir de su radio'
print '*'*80

#Entrada de datos, pedimos el radio al usuario
radio = input ('Introduzca el radio de la circunferencia: ')

#Realizamos los calculos ncesarios
area = 4*pi*radio**2
# volumen = 4/3.*pi*radio**3
volumen = float(4)/3*pi*radio**3

#Mostramos resultado
print 'Una esfera con radio:', radio
print 'tiene un area de:', round(area,2)
print 'y un volumen de:', round(volumen,2)

#Fin
raw_input ('Pulse intro para salir')
