# -*- coding: cp1252 -*-


suma = 0.0
contador = 0
numero = raw_input("introduzca número >>> ")


while numero != '':
    suma = suma + int(numero)
    contador = contador + 1
    numero = raw_input("introduzca número >>> ")

# fuera del bucle
if contador == 0:
    print "No se han introducido datos"
else:
    print "La media es", suma / contador
    
    
