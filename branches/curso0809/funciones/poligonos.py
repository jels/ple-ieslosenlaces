"""
Ejercicio de funciones de pol�gonos
"""

def cuadrilatero(lado1, lado2):
    """ Imprime per�metro y �rea
"""
    perim = lado1 * 2 + lado2 * 2
    area = lado1 * lado2
    print 'Per�metro', perim
    print '�rea', area

def pedir_datos():
    lado1 = input("Introduce el primer lado: ")
    lado2 = input("Introduce el segundo lado: ")
    return lado1, lado2

l1, l2 = pedir_datos()
cuadrilatero(l1, l2)
   
