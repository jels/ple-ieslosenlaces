# -*- encoding: utf-8 -*-

from funciones import area, circunferencia
from graphics import *

ventana = GraphWin("Círculo", 800, 600)

ventana.setCoords(-10,-10, 10, 10)

Text(Point(-8, 9), "Introduzca el radio").draw(ventana)
radioEntry = Entry(Point(-8, 8), 5)
radioEntry.draw(ventana)

Text(Point(-7, 5), "Haz clic para continuar").draw(ventana)

ventana.getMouse()

radio = float(radioEntry.getText())

radio_area = area(radio)
radio_circunf = circunferencia(radio)

Text(Point(-7, 0), "Circunferencia = %.2f" % radio_circunf).draw(ventana)

Text(Point(-7, -1), "Área círculo = %.2f" % radio_area).draw(ventana)

circulo = Circle(Point (3,0), radio%8)
circulo.draw(ventana)


Text(Point(-7, -9), "Haz clic para terminar").draw(ventana)
ventana.getMouse()
ventana.close()



     
