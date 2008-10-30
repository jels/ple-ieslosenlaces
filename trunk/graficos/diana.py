
"""
Dibujando una diana de arco con graphics
"""

from graphics import *

ventana = GraphWin("Tablero de ajedrez", 400, 400)
ventana.setCoords(-12, -12, 12 , 12 )
ventana.setBackground('white')
colores = ['white', 'white', 'black', 'black', 'blue', 'blue', 'red', 'red',
           'yellow', 'yellow']
for x in range(10):
    c = Circle(Point(0,0), 10-x)
    c.setFill(colores[x])
    c.draw(ventana)
Point(0,0).draw(ventana)
    
    