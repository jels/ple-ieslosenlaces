# -*- coding: cp1252 -*-
# Ejercicio ordenar tres n�meros

from easygui import *
import sys

# Captura de los datos
#num1 = raw_input("Introduzca primer n�mero: ")
num1 = enterbox("Introduzca n�mero")
if num1 == None:
    msgbox("Has cancelado la operaci�n. Bye")
    sys.exit()
if num1 == "":
    msgbox("No has introducido nada. Bye")
    sys.exit()
num1 = int(num1)
num2 = raw_input("Introduzca segundo n�mero: ")
num2 = int(num2)
num3 = raw_input("Introduzca tercer n�mero: ")
num3 = int(num3)

# Ordenar
if num1 > num2:
    if num1 > num3:
        if num2 > num3:
            res = (num1, num2, num3)
        else:
            res = (num1, num3, num2)
    else:
        res = (num3, num1, num2)
else:
    if num3 > num1:
        if num2 > num3:
            res = (num2, num3, num1)
        else:
            res = (num3, num2, num1)
    else:
        res = (num2, num1, num3)

# Mostrar resultado
print 'N�meros ordenados: ',
for x in res:
    print x,
print
#### Ordenar con python
numeros = [num1, num2, num3]
numeros.sort(reverse = True)
print 'N�meros ordenados (v.2): ',
for x in numeros:
    print x,
print



