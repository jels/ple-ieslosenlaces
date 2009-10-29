# -*- coding: cp1252 -*-

def multiplos_de(x):
    """
    multiplos_de(x) --> Imprime multiplos de x menores que 100

    Explicación ampliada
    """
    for n in range(1, 100):
        if n % x == 0:
            print n,
    print
            

# test del programa
num = raw_input("Intro número: ")
num = int(num)
multiplos_de(num)
