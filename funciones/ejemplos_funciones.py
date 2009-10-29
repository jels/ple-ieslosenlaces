# -*- coding: cp1252 -*-
from turtle import *

# Definición de la función cuadrado
def cuadrado(lado):
    for x in range(4):
        fd(lado)
        rt(90)

# ejecutar función cuadrado
for x in range(5, 200, 10):
    cuadrado(x)
raw_input()
