# -*- coding: cp1252 -*-



'''
Escribe un programa sumatorio.py
que calcule la suma de los primeros n números naturales,
donde n es un valor que introducirá el usuario

AUTOR: PABLO MARTIN
VERSION: 1.0

'''


# Introduccion al programa
print 'Hola, Este programa sumara todos los numeros naturales hasta un valor\
 dado por usted '
print '*'*80

# Introduccion de datos del usuario
n = input (' Introduzca un numero natural ')

#Operaciones
suma = 0
for numero in range (n+1):
    suma = suma + numero
    #Mostrar resultados de todo el proceso y final
print ' La suma de los numeros naturales hasta ', n, ' es ', suma

#Fin
raw_input (' Pulse intro para salir ')
