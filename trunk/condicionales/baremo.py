# -*- coding: cp1252 -*-
"""
Un profesor pone un test de 100 preguntas, que se bareman
de la siguiente forma: de 90 a 100: A, 80-89: B, 70-79:C,
60-69:D, <60:F. Escribe un programa que pida la puntuación
y muestre el equivalente en letra.
"""
from easygui import *

nota = enterbox("Introduzca nota")
nota = float(nota)

if nota >= 90:
    res = "A" 
elif nota >= 80:
    res = "B"
elif nota >= 70:
    res = "C"
elif nota >= 60:
    res = "D"
else:
    res = "F"

msgbox("Tu nota es " + res)
