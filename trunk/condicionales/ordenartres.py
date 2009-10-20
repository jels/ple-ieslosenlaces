# -*- coding: cp1252 -*-
# Ejercicio ordenar tres números

from easygui import *
import sys

# Captura de los datos
#num1 = raw_input("Introduzca primer número: ")
num1 = enterbox("Introduzca número")
if num1 == None:
    msgbox("Has cancelado la operación. Bye")
    sys.exit()
if num1 == "":
    msgbox("No has introducido nada. Bye")
    sys.exit()
num1 = int(num1)
num2 = raw_input("Introduzca segundo número: ")
num2 = int(num2)
num3 = raw_input("Introduzca tercer número: ")
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
print 'Números ordenados: ',
for x in res:
    print x,
print
#### Ordenar con python
numeros = [num1, num2, num3]
numeros.sort(reverse = True)
print 'Números ordenados (v.2): ',
for x in numeros:
    print x,
print



