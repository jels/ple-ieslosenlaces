# -*- coding: cp1252 -*-
"""Ejemplo que maneja dos tortugas ...
"""

from turtle import *
from random import randint  # genera números aleatorios
import time

t1 = Turtle()
t2 = Turtle()
t1.shape('turtle')
t1.up()
t1.setpos(-100,0)

t2.up()
t2.setpos(100,0)

while True: # bucle infinito
    t1.setpos(randint(-200, 200), randint(-200, 200))
    t2.setpos(randint(-200, 200), randint(-200, 200))
    
    time.sleep(1)  # tiempo de espera entre movimientos
