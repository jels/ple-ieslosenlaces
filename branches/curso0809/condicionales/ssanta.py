
"""
Calcula el d�a de la semana santa
F�rmula normal: a�os entre 1982 y 2048 (inc.)

Para a�os entre 1900 y 2099: 1954, 1981, 2049
    y 2076: una semana m�s tarde.

"""

import sys


def calcula_s_santa(year):
    """
    Imprime el d�a del domingo de pascua ...

    >>> calcula_s_santa(2009)
    '12 de abril'
    """
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19*a + 24) % 30
    e = (2*b+4*c + 6*d +5) % 7
    dia = 22 + d + e
    if dia > 31:
        print dia - 31, 'de abril'
    else:
        print dia, 'de marzo'

def 

year = int(raw_input("Introduzca el a�o: "))

# comprobar que el a�o es v�lido
if year < 1982 or year > 2048:
    print "A�o no v�lido"
else:
    calcula_s_santa(year)


