# -*- encoding: utf-8 -*-

from graphics import *
from time import sleep

"""
Ejemplo de uso de la librería graphics de zelle
Descargar de http://mcsp.wartburg.edu/zelle/python/graphics.py

Necesita optimizar el código.
"""

# crear ventana
ventana = GraphWin("Ejercicio semáforo")

# caja del semáforo.
caja = Rectangle(Point(50, 5), Point(150, 195))
caja.setFill('black')
caja.draw(ventana)

# puntos para las luces
p1 = Point(100, 40)
p2 = Point(100, 100)
p3 = Point(100, 160)

# tres discos: fondo blanco, bode del disco
rojo = Circle(p1, 25)
rojo.setOutline('red')
rojo.setFill('white')

amarillo = Circle(p2, 25)
amarillo.setOutline('yellow')
amarillo.setFill('white')

verde = Circle(p3, 25)
verde.setOutline('green')
verde.setFill('white')

# coloca discos en caja
discos = [rojo, amarillo, verde]

for d in discos:
    d.draw(ventana)

# ciclo encender / apagar
while 1:
    rojo.setFill('red')
    sleep(2)
    rojo.setFill('white')
    verde.setFill('green')
    sleep(2)
    verde.setFill('white')
    amarillo.setFill('yellow')
    sleep(1)
    amarillo.setFill('white')

