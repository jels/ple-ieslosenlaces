# -*- coding: cp1252 -*-

# Indicamos que utilice el módulo turtle
from turtle import *

screen = Screen()
screen.tracer(1, 0)
ht()


lt(90)

for x in range(9):
    pencolor("black")
    for x in range(40):
        fd(100)
        bk(100)
        rt(0.5)

    pencolor("red")

    for a in range(40):
        fd(100)
        bk(100)
        rt(0.5)
