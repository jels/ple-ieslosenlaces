# -*- coding: cp1252 -*-

def sumatorio(x):
    """
    sumatorio (x) --> devuelve sumatorio
    """
    suma = 0
    for n in range(1, x+1):
        #suma = suma + n
        suma += n
    return suma

num = raw_input('Intro. núm: ')
num = int(num)
print sumatorio(num)


    
