# -*- encoding: utf-8 -*-
'''
Created on 19/11/2009

@author: dai
'''

from auxliga import *
from auxgrafico import *



# leer datos y preparar matriz
# datos_liga --> matriz con datos del fichero
datos_liga = crea_tabla(r'datos\liga09.csv')

# ej1. imprimir datos_liga: equipo y puntos
# por orden alfab�tico
puntos_equipos(datos_liga)

# ej2. imprimir datos_liga: equipo y puntos
# por orden en tabla de clasificaci�n
datos_liga.sort(ordena_puntos)  # ordena matriz
print 
print '*' * 20
print
puntos_equipos(datos_liga)
    
# imprime s�lo nombres
nombres_equipos = nombres(datos_liga)
print sorted(nombres_equipos)

grafico([], 'Mejores equipos')