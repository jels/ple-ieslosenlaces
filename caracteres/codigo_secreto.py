# -*- coding: cp1252 -*-

import os

# Inicializamos la variable para entrar en el bucle
o = 1

# Entramos en el bucle, en el cual seguiremos siempre que la opcion sea 1 o 2
while o == 1 or o == 2:
    # Imprimimos el menú con las opciones
    print "\n\nCodificador // Decodificador"
    print "\n Opciones: \n"
    print "\t1) Codificar"
    print "\t2) Decodificar"
    print "\n\t** Cualquier otra opcion sale"
    # El usuario eligirá una
    o = input("\n\n Selecciona una opcion: ")
    # Limpiamos la pantalla
    os.system('cls')

    # Si la opción elegida es 1 entraremos en la fase de codificacion
    if o == 1:
        # Pedimos la frase
        frase = raw_input("\n\nIntroduce una frase: ")
        codigo = ''

        # Codificamos la frase y la guardamos en la variable codigo
        for x in range(len(frase)):
            codigo += chr(ord((frase[x]))+1)

        # Mostramos el resultado
        print "\n\nLa frase codificada es: ",codigo
        # Paramos la ejecución para poder ver el resultado en pantalla
        raw_input()
        # Y limpiamos la pantalla
        os.system('cls')

    # Si la opción elegida es 2 entraremos en la fase de decodificacion
    if o == 2:
        frase = ''
        # Pedimos la frase codificada
        codigo = raw_input("\n\nIntroduce la frase codificada: ")
        
        # Decodificamos la frase codificada y la guardamos en la variable frase
        for x in range(len(codigo)):
            frase += chr(ord((codigo[x]))-1)
            
        # Mostramos el resultado
        print "\n\nLa frase decodificada es: ",frase
        # Paramos la ejecución para poder ver el resultado en pantalla
        raw_input()
        # Y limpiamos la pantalla
        os.system('cls')
