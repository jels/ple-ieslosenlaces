# -*- coding: utf-8 -*-

from math import sqrt

def es_primo_adrian(numero):
    """
    Devuelve verdadero si el número es primo. Si no,
    devuelve falso.
    """
    contador = 2
    primo = True
    while (primo) and contador != numero:
        if numero % contador == 0:
            primo = False
        contador = contador +1
    return primo

def es_primo_pablo(numero):
    for x in range(2,round(sqrt(numero)) +1 ):
        if numero % x == 0:
            return False
    return True

    
contador = 0
numero = 2
while contador < 10:
    if es_primo_pablo(numero):
        print numero
        contador = contador +1
    numero = numero + 1
        
