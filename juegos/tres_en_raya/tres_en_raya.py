# -*- coding: cp1252 -*-
"""Juego tres en raya ....
"""

# definiciones de funciones
def muestra_instrucciones():
    print ''' Al juego se juega así:
blablabla,
blablabla,

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
        tablero.append('.')
    return tablero

def mostrar_tablero(t):
    print '\t', t[0], '|', t[1], '|', t[2]
    print '\t', '-' * 11
    print '\t',t[3], '|', t[4], '|', t[5]
    print '\t', '-' * 11
    print '\t',t[6], '|', t[7], '|', t[8]

def movimientos_legales(tablero):
    '''Devuelve una lista con los movimientos legales disponibles 0-8'''
    legales = []
    # recorro tablero
    return legales


def posiciones_ganadoras():
    pass

# juego

muestra_instrucciones()
print inicia_jugador()
# crea tablero vacío
tablero = nuevo_tablero()
tablero[0] = 'X'
tablero[4] = 'X'
tablero[8] = 'X'
mostrar_tablero(tablero)


    
