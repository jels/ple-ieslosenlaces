# -*- coding: cp1252 -*-
"""
Escribe un programa escribe100.py que escriba en un fichero
llamado 100.txt los números del 1 al 100, separados por un
espacio en blanco.
"""

# 1. preparar fichero escritura
f = open('100.txt', 'w')

# 2. generar números --> escribir en fichero
for num in range(1, 101):
    f.write(str(num) + ' ')

# 3. cerrar fichero
f.close()
