# -*- encoding: utf-8 -*-

"""
Muestra numerados los nombres de alumnos escritos en un fichero. 
(un alumno por línea)
"""

nom_fich = raw_input("Introduce nombre fichero: ")

f_lect = open(nom_fich)

contador = 1

for alumno in f_lect:
    print "%2d: %s" % (contador, alumno),
    contador = contador +1

f_lect.close()

