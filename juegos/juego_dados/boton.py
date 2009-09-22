# -*- encoding: cp1252 -*-
"""
Clase Boton
para graphics
"""

from graphics import *

class Boton(object):
    """
    Crea un botón rectangular
    bot = Boton(ventana, Point(30,20), 20, 10, 'Salir')
    Boton(ventana, centro, ancho, alto, etiqueta)
    """
    def __init__(self, ventana, centro, ancho, alto, etiqueta):
        w, h = ancho/2, alto/2
        x, y = centro.getX(), centro.getY()
        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(ventana)
        self.etiqueta = Text(centro, etiqueta)
        self.etiqueta.draw(ventana)
    def tocado(self, p):
        """
        Devuelve verdadero si el punto p está dentro del rectángulo
        """
        if p.getX()>= self.xmin and p.getX()<= self.xmax and \
           p.getY() >= self.ymin and p.getY() <= self.ymax:
            return True
        else:
            return False
        
    


        
        
    
