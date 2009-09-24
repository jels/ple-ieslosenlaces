# -*- coding: cp1252 -*-
from turtle import *

# Ejercicio triángulo
lt(90) # Colocar posición inicial


# num lados:
lados = input("Lados de la figura: ")
for x in range(lados):
    fd(100)
    rt(360/lados)
    

raw_input()

    
