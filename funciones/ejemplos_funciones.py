# -*- coding: cp1252 -*-
from turtle import *

# Definici�n de la funci�n cuadrado
def cuadrado(lado):
    for x in range(4):
        fd(lado)
        rt(90)

# ejecutar funci�n cuadrado
for x in range(5, 200, 10):
    cuadrado(x)
raw_input()
