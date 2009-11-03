# -*- coding: cp1252 -*-
"""Juego tres en raya ....
"""

import time   # Retardo cuando juega el ordenador

# definiciones de funciones
def muestra_instrucciones():
    print ''' Al juego se juega así:
Posiciones:

 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
 
'''
def inicia_jugador():
    '''inicia_jugador () --> True/False

Pregunta al jugador si quiere comenzar moviendo la primera ficha
'''
    resp = raw_input('¿Comienzas tú el juego? (s/n)')
    if resp.lower() == 's' or resp.lower() == 'si':
        return True
    else:
        return False

def nuevo_tablero():
    '''nuevo_tablero() --> tablero
'''
    tablero = []
    for x in range(9):
        tablero.append(' ')
    return tablero

def mostrar_tablero(t):
    print '\t  ', t[0], '|', t[1], '|', t[2]
    print '\t ', '-' * 11
    print '\t  ',t[3], '|', t[4], '|', t[5]
    print '\t ', '-' * 11
    print '\t  ',t[6], '|', t[7], '|', t[8]

def movimientos_legales(tablero):
    '''Devuelve una lista con los movimientos legales disponibles 0-8'''
    legales = []
    for x in range(len(tablero)):
        if tablero[x] == ' ':
            legales.append(x)
    # recorro tablero
    return legales

def posiciones_ganadoras():
    ganadoras = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7], 
        [2,5,8],
        [0,4,8],
        [2,4,6]
        ]
    return ganadoras

def ganador(t):
    '''
    Busca en tablero combinación ganadora.
    Si la encuentra, devuelve ficha,
    Si no: devuelve None
    '''
    formas_de_ganar = posiciones_ganadoras()
    for fila in formas_de_ganar:
        if t[fila[0]] == t[fila[1]] == t[fila[2]] != ' ':  # ojo con las casilla vacías
            return t[fila[0]]
    return None

    
    
def pregunta_movimiento(tablero):
    """Devuelve posición legal: 0-8
    """
    legales = movimientos_legales(tablero)
    #print 'legales -->', legales
    pos = int(raw_input('Introduce una posición (1-9): '))
    while pos-1 not in legales:
        pos = int(raw_input('Posición ocupada. \nIntroduce una posición (1-9): '))
    return pos -1


    

def test():
    # juego probatinas
    muestra_instrucciones()
    print inicia_jugador()
    # crea tablero vacío
    tablero = nuevo_tablero()
    print 'Ninguno', ganador(tablero)
    tablero[0] = 'X'
    tablero[4] = 'X'
    tablero[8] = 'X'
    mostrar_tablero(tablero)
    print 'X -->', ganador(tablero)
    print pregunta_movimiento(tablero)
    mostrar_tablero([1, 2, 3, 'X', 'X', 6, 7, 'O', 9])


def mueve_ordenador(tablero, ordenador, jugador):
    ''' mueve_ordenador(tablero, ordenador, jugador) --> devuelve movimiento (0-8).
    Toma como datos: el tablero, la ficha con la que juega el ordenador y
    la ficha con la que juega el jugador.
    Estrategia del ordenador:
    Estrategia básica:

       1. Si hay un movimiento gandador, el ordenador debe elegirlo
       2. Si el humano tiene un movimiento ganador en la próxima jugada, el ordenador tien que elegirlo.
       3. Si no, tiene que elegir la posición más ventajosa: el centro, las esquinas y el resto.
    '''
    libres = movimientos_legales(tablero)
    t = tablero[:]  # copia del tablero de juego: ojo con efectos laterales!!!
    for pos in libres:
        t[pos] = ordenador
        if ganador(t) == ordenador:
            return pos  # bien!! he ganado :-D
        else:
            t[pos] = ' '  # vuelvo a dejar la casilla libre
    for pos in libres:   # Evito que gane el jugador
        t[pos] = jugador
        if ganador(t) == jugador:
            return pos  # Cuidado que si no me ganan!!!
        else:
            t[pos] = ' '  # vuelvo a dejar la casilla libre
    MEJORES_POSICIONES = [4, 0, 2, 6, 8, 1, 3, 5, 7]
    for m in MEJORES_POSICIONES:
        if m in libres:
            return m  # devuelvo la menos mala
    



def main():
    muestra_instrucciones()
    tablero = nuevo_tablero()
    if inicia_jugador()== True:
        jugador, ordenador = 'X','O'
    else:
        jugador, ordenador = 'O','X'
    turno = 'X'
    mostrar_tablero(tablero)
    while not ganador(tablero) and len(movimientos_legales(tablero)) > 0:   # Entra en el bucle cuando ganador devuelve None
        if turno == jugador:
            pos = pregunta_movimiento(tablero)
            tablero[pos] = jugador
        else:
            time.sleep(1)
            print 'Estoy pensando ....'
            pos = mueve_ordenador(tablero, ordenador, jugador)
            tablero[pos] = ordenador
        mostrar_tablero(tablero)
        if turno == 'X':
            turno = 'O'
        else:
            turno = 'X'
        

    
    








main()
    
