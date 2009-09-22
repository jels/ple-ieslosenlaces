# -*- encoding: cp1252 -*-
"""
Clase Dado
Muestra un dado en el entorno graphics
"""

from graphics import *

class Dado(object):
    """
    Dibuja un dado de 6 caras
    """
    def __init__(self, ventana, centro, tam):
        """
        Dibuja la cara de un dado
        Dado(ventana, centro, tam)
        """
        self.ventana = ventana
        self.fondo = "white"
        self.color = "black"
        self.ptam = tam * 0.1  # Tamaño del punto
        distancia = tam * 0.3 # distancia del punto al centro
        # creamos cuadrado de la cara
        cx, cy = centro.getX(), centro.getY()
        p1 = Point(cx-tam/2., cy-tam/2.)
        p2 = Point(cx+tam/2., cy+tam/2.)
        rect = Rectangle(p1, p2)
        rect.draw(ventana)
        rect.setFill(self.fondo)

        self.puntos = []
        pos = {1:[-1,  -1], 2:[-1, 0], 3:[-1, 1],
               4:[0, 0], 5:[1, -1], 6:[1, 0], 7:[1,1]}
        for x in range(1, 8):
            self.puntos.append(self.__creaPunto(cx+pos[x][0]*distancia,
                                                cy+pos[x][1]*distancia))
        self.ponValor(1)

    def __creaPunto(self, x, y):
        """
        Método privado
        """
        punto = Circle(Point(x,y), self.ptam)
        punto.setFill(self.fondo)
        punto.setOutline(self.fondo)
        punto.draw(self.ventana)
        return punto
    def ponValor(self, valor):
        for p in self.puntos:
            p.setFill(self.fondo)  ## Borra los puntos
        color_valor = {1:[4], 2:[1, 7], 3:[1, 4, 7],
                       4:[1, 3, 5, 7], 5:[1, 3, 4, 5, 7],
                       6:[1, 2, 3, 5, 6, 7 ]}
        for n in color_valor[valor]:
            self.puntos[n-1].setFill(self.color)
    
        
    
        
        
        
        


        
