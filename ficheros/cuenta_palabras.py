# -*- coding: cp1252 -*-
"""
Escribe un programa cuenta_palabras.py, que pedir� el nombre de
un fichero y mostrar� el n�mero de l�neas, de palabras y de
caracteres que contiene el fichero.

POR HACER / TODO
Corregir cuando fichero est� vac�o:  marca una l�nea
"""
import os

# pedir nombre fichero
nombre = raw_input("Introduce nombre fichero: ")

# comprobar si existe
if os.path.exists(nombre):
    # abrir fichero modo lectura
    f = open(nombre)
    contenido = f.read()

    # contar l�neas
    print 'N�mero de l�neas', len(contenido.split('\n'))

    # contar palabras
    print 'N�mero de palabras', len(contenido.split())

    # contar caracteres
    print 'N�mero de caracteres', len(contenido)
else:
    print "El fichero <" + nombre + "> no existe."
