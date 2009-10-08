# -*- coding: cp1252 -*-
'''Escribe un programa lee100.py que lea el fichero
anteriormente creado (100.txt) y lo muestre en la pantalla'''


# 1. Preparar lectura
f = open('100.txt')

# 2. leer fichero
numeros = f.read()

# tamaño de la cadena
print 'Tamaño del fichero: ', len(numeros)

# 2.2. cambiar espacio por salto
#numeros = numeros.replace(' ', '\n')
numeros = numeros.split()
for n in numeros:
    print n
# 3. mostrar
#print numeros

f.close()
