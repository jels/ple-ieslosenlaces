# -*- coding: cp1252 -*-
"""
Escribe un programa cuenta_palabras.py, que pedirá el nombre de
un fichero y mostrará el número de líneas, de palabras y de
caracteres que contiene el fichero.

POR HACER / TODO
Corregir cuando fichero está vacío:  marca una línea
"""
import os

# pedir nombre fichero
nombre = raw_input("Introduce nombre fichero: ")

# comprobar si existe
if os.path.exists(nombre):
    # abrir fichero modo lectura
    f = open(nombre)
    contenido = f.read()

    # contar líneas
    print 'Número de líneas', len(contenido.split('\n'))

    # contar palabras
    print 'Número de palabras', len(contenido.split())

    # contar caracteres
    print 'Número de caracteres', len(contenido)
else:
    print "El fichero <" + nombre + "> no existe."
