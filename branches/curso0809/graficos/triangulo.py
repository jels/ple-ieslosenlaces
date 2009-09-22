# -*- encoding: utf-8 -*-
"""
Dibuja un polígono en la pantalla
y lo rellena de color
"""

from graphics import *

ventana = GraphWin("Polígono")
Text(Point(25, 15), 'Color:').draw(ventana)
color = Entry(Point(120, 15), 10)
color.draw(ventana)
Text(Point(195, 100), "Cierra la ventana para terminar").draw(ventana)
while True:
    p1 = ventana.getMouse()
    p2 = ventana.getMouse()
    p3 = ventana.getMouse()
    tri = Polygon(p1,p2, p3)
    tri.setFill(color.getText())
    tri.draw(ventana)


