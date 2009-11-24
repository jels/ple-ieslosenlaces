# -*- encoding: utf-8 -*-
'''
Created on 19/11/2009

@author: dai
'''
from graphics import *


def lineas(ventana, xmax, ymax):
    lx = Line(Point(0,0), Point(xmax, 0))
    lx.draw(ventana)
    lx.setWidth(3)
    ly = Line(Point(0,0), Point(0, ymax))
    ly.draw(ventana)
    ly.setWidth(3)
    for num in range(5, ymax+1, 5):
        t = Text(Point(-0.5, num), str(num))
        t.draw(ventana)

def dibuja_barra(ventana, posx, posy):
    ''' dibuja una barra en posx de altura
    posy
    '''
    barra = Rectangle(Point(posx, 0), 
                      Point(posx+1, posy))
    barra.draw(ventana)
    barra.setFill('red')
    barra.setOutline('white')
    
def leyenda(ventana, datos):
    posx = 0.5
    for le in datos:
        t = Text(Point(posx, -1),le[:4])
        t.draw(ventana)
        t.setSize(8)
        posx += 1
                

def grafico(datos, titulo="Gráfica de la liga"):
    '''grafico genera una gráfica de barras con 
    la tabla datos
    datos tendrá la estructura: nombre - valor
    '''
    win = GraphWin(titulo, 400, 400)
    # Prepara coordenadas:
    win.setCoords(-2, -5, 7, 35)
    win.setBackground('white')
    # Hacer el gráfico
    
    pos = 0
    for equipo in datos:
        dibuja_barra(win, pos, equipo[1])
        pos += 1
    lineas(win, 6.5, 30)
    datos_leyenda = []
    for eq in datos:
        datos_leyenda.append(eq[0])
    leyenda(win, datos_leyenda)
    win.getMouse()
    