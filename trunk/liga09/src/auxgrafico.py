# -*- encoding: utf-8 -*-
'''
Created on 19/11/2009

@author: dai
'''
from graphics import *

def grafico(datos, titulo="Gr�fica de la liga"):
    '''grafico genera una gr�fica de barras con 
    la tabla datos
    datos tendr� la estructura: nombre - valor
    '''
    win = GraphWin(titulo, 400, 400)
    # Hacer el gr�fico
    
    win.getMouse()
    