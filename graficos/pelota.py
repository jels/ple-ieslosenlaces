"""

"""
from graphics import *
from time import sleep

ANCHO = 300
ALTO = 200
ventana = GraphWin("Pelota", ANCHO, ALTO)
p = Image(Point(100,100), "pelota.gif")
p.draw(ventana)
dx = dy = 1
for x in range(10000):
    pos = p.getAnchor()
    if pos.getX() < 10:
        dx = 1
    if pos.getX() > ANCHO -1:
        dx = -1
    if pos.getY() < 10:
        dy = 1
    if pos.getY() > ALTO -10:
        dy = -1
    p.move(dx,dy)
    sleep(0.005)
    
    
