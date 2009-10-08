# -*- coding: cp1252 -*-
"""
Escribe un programa que pida la nota de un alumno.
Si la nota es menor que 5, el programa mostrará el mensaje: "suspenso"
"""

from easygui import *

nota = enterbox("Introduzca nota")
nota = float(nota)

if nota < 5:
    msgbox("Has suspendido :-(")
else:
    msgbox("Has aprobado :-)")
