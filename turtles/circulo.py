# -*- coding: cp1252 -*-
"""
Ejemplo para quitar animación a tortugas ...
"""
from turtle import *

screen = Screen()
screen.tracer(5, 10)

screen.bgcolor('orange')
for x in range(180):
    fd(2)
    rt(2)
    
