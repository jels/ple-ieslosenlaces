

"""
c�lculo m�ximo com�n divisor
algoritmo de euclides
"""

def mcd(a, b):
    """
    x es el mayor
    """
    while b != 0:
        aux = b
        b = a % b
        a = aux
    return a

def main():
    x, y = input("Introduce dos n�meros: ")
    if x > y:
        print mcd(x,y)
    else:
        print mcd(y, x)
    
main()
