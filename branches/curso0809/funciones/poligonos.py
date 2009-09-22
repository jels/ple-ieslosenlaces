"""
Ejercicio de funciones de polígonos
"""

def cuadrilatero(lado1, lado2):
    """ Imprime perímetro y área
"""
    perim = lado1 * 2 + lado2 * 2
    area = lado1 * lado2
    print 'Perímetro', perim
    print 'Área', area

def pedir_datos():
    lado1 = input("Introduce el primer lado: ")
    lado2 = input("Introduce el segundo lado: ")
    return lado1, lado2

l1, l2 = pedir_datos()
cuadrilatero(l1, l2)
   
