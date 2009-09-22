# -*- coding: cp1252 -*-
"""
Escribe un programa media_usuario.py que calcule la media de una serie de n�meros introducidos por el usuario. Como en el programa anterior, programa preguntar� primero cu�ntos n�meros va a introducir y despu�s pedir� los n�meros al usuario. Nota: la media ser� un n�mero float. 
"""

#Pedimos los datos al usuario
cantidad = input('�Cu�ntos n�meros vas a introducir? ')

#Realizamos las operaciones necesarias
resultado = 0
for num in range (1, cantidad+1):
    print 'Introduce el valor', num, ':'
    auxiliar = input()
    resultado = resultado + auxiliar

media = resultado / float(cantidad)

#Mostramos el resultado por pantalla
print 'La media de los valores introducidos es', round(media,2)

#Fin
raw_input('Pulse Intro para terminar...')
