from graphics import GraphWin, Point
from boton import Boton
from dado import Dado
import random

def main():
    """
    Estructura principal
    """
    win = GraphWin("Juego de dados")
    win.setCoords(0,0,10,10)
    win.setBackground("green")

    # crear dados
    dado1 = Dado(win, Point(3,7), 2)
    dado2 = Dado(win, Point(7,7), 2)

    # crear botones
    boton_tirar = Boton(win, Point(5, 4), 6, 2, "Tirar Dados")
    boton_salir = Boton(win, Point(5, 1), 2, 2, "Salir")

    # Bucle principal
    while True:
        p = win.getMouse()
        if boton_tirar.tocado(p):
            valor1 = random.randrange(1, 7)
            valor2 = random.randrange(1, 7)
            dado1.ponValor(valor1)
            dado2.ponValor(valor2)
            
        elif boton_salir.tocado(p):
            break
    
    win.close()

if __name__ == '__main__':
    main()
