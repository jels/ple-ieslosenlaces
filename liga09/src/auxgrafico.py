# -*- encoding: utf-8 -*-
'''
Created on 19/11/2009

@author: dai
'''
from graphics import *

def grafico(datos, titulo="Gráfica de la liga"):
    '''grafico genera una gráfica de barras con 
    la tabla datos
    datos tendrá la estructura: nombre - valor
    '''
    win = GraphWin(titulo, 400, 400)
    # Hacer el gráfico
    
    win.getMouse()
    