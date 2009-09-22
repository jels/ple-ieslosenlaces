# -*- coding: utf-8 -*-

"""
Recoge número positivos
Calcula la suma
Dice cuántos números válidos se han introducido
"""

contador = 0 # contará los números introducidos
suma = 0  # para sumar los números

numero = input("Introduzca número (positivo): ")
menor = numero
mayor = numero

while numero >= 0:
    contador = contador + 1
    suma = suma + numero
    if numero < menor:
        menor = numero
    numero = input("Introduzca número (positivo): ")

print '*'*10, 'resumen', '*'*10
print 'Ha introducido', contador, 'números'
print 'Suman', suma
print 'Menor', menor

    
