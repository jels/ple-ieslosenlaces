# -*- encoding: utf-8 -*-

"""
Sobre el ejemplo de J. Zelle

# futval_graph.py
#    A program to compute the value of an investment
#    carried 10 years into the future
"""

from graphics import *

# Introducción
print "El programa dibuja el crecimiento de una inversión a 10 años."

# Datos de capital inicial y de interés
inicial = input("Introduce el capital inicial: ")
interes = input("Introduce el interés (3, 4, 5.5 ...): ")
interes = interes/100.

# Crea una ventana gráfica con las etiquetas en la izquierda.
win = GraphWin("Gráfico de crecimiento de una inversión", 320, 240)
win.setBackground("white")
Text(Point(20, 230), ' 0.0K').draw(win)
Text(Point(20, 180), ' 2.5K').draw(win)
Text(Point(20, 130), ' 5.0K').draw(win)
Text(Point(20, 80), ' 7.5k').draw(win)
Text(Point(20, 30), '10.0K').draw(win)

# Dibuja barra de capital inicial.
altura = inicial * 0.02
bar = Rectangle(Point(40, 230), Point(65, 230-altura))
bar.setFill("green")
bar.setWidth(2)
bar.draw(win)

# Dibuja las barras para los años siguientes
for year in range(1,11):
    # Calcula el valor para el próximo año
    inicial = inicial * (1 + interes)
    # dibuja nueva barra para este valor
    pos_x = year * 25 + 40
    altura = inicial * 0.02
    bar = Rectangle(Point(pos_x, 230), Point(pos_x+25, 230-altura))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

raw_input("Pulsa <Intro> para terminar.")
win.close()

