from graphics import *

ventana = GraphWin("Tablero de ajedrez", 400, 400)
ventana.setCoords(0, 0, 8, 8)
ventana.setBackground('white')

# columnas que empiezan con cuadro negro
for x in range(0,8,2):
    for y in range(0,8,2):
        r = Rectangle(Point(x,y), Point(x+1,y+1))
        r.setFill('black')
        r.draw(ventana)

# columnas que empiezan con cuadro blanco
for x in range(1,8,2):
    for y in range(1,8,2):
        r = Rectangle(Point(x,y), Point(x+1,y+1))
        r.setFill('black')
        r.draw(ventana)


