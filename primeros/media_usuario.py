# -*- coding: cp1252 -*-
"""
Escribe un programa media_usuario.py que calcule la media de una serie de números introducidos por el usuario. Como en el programa anterior, programa preguntará primero cuántos números va a introducir y después pedirá los números al usuario. Nota: la media será un número float. 
"""

#Pedimos los datos al usuario
cantidad = input('¿Cuántos números vas a introducir? ')

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
