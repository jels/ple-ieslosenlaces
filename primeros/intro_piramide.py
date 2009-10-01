# -*- coding: cp1252 -*-
"""Repeticiones dentro de repeticiones

Ejercicio de ayuda para construir la pirámide
"""

TOTAL = 12  # Número de filas que tiene la figura
for fila in range(TOTAL):
    print 'fila', fila+1, ':',
    for celda in range(fila+1):  # Columnas dentro de la fila
            print 'c.', celda,
    print  # Hace el salto de fila a la fila siguiente

# Ejemplo pirámide
for fila in range(TOTAL):
    for celda in range(fila+1):  # Columnas dentro de la fila
            print '*',
    print


