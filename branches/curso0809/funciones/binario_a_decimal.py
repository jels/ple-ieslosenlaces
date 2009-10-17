# -*- encoding: utf-8 -*-

""" Convierte de sistema de numeración binario a decimal

Lee el número binario como una cadena de caracteres (es lo que sabemos recorrer
por ahora). Multiplica cada posición (convertida a int) por la potencia de 2
correspondiente. 

Convertido a una función
"""

# num_binario: la cadena de caracteres que podremos recorrer


def convierte_binario(num_binario):
    """
    convierte_binario(binario) --> imprime número decimal
    """
    num_digitos = len(num_binario)  # dígitos binarios

    num_decimal = 0 # inicializamos para sumar el valor de los dígitos
    exponente = num_digitos - 1 # potencia de 2 del primer dígito de la izquierda

    # Extraemos los dígitos de izquierda a derecha
    for d in num_binario:
        d_int = int(d)  # el dígito d es una cadena de caracteres. Hay que convertirla
        num_decimal = num_decimal + d_int * 2**exponente
        exponente = exponente -1 # exponente para el siguiente dígito.
        
    print "%s --> %d" % (num_binario, num_decimal)


convierte_binario('111')