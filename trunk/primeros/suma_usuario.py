# -*- coding: cp1252 -*-
"""
Escribe un programa suma_usuario.py que sume una serie de n�meros introducidos
por el usuario. El programa preguntar� primero cu�ntos n�meros va a introducir
y despu�s pedir� los n�meros al usuario.
AUTOR: Jes�s Mart�nez
"""

#Se piden los datos de entrada al usuario
cantidad = input('�Cu�ntos n�meros vas a introducir? ')

#Realizamos las operaciones necesarias
resultado = 0
for num in range (1, cantidad+1):
    #print 'Introduce el valor', num, ':',
    #auxiliar = input()
    auxiliar = input('Introduce el valor '+ str(num) + ': ')
    resultado = resultado + auxiliar

#Mostramos el resultado por pantalla
print 'El sumatorio total es', resultado, '.'

#Fin
raw_input('Pulse Intro para terminar...')
