"""
Ejercicio Ahorcado

"""

import random
def obtener_palabra():
    """
    Devuelve palabra
    """
    return random.choice(("hola", 'adios'))

def muestra_resultado(oculta, introducidas, errores):
    faltan = 0
    for letra in oculta:
        if letra in introducidas:
            print letra,
        else:
            print '_',
            faltan = faltan +1
    print
    print errores, 'errores'
    return faltan
    

def main():
    introducidas = ""  # letras introducidas por el usuario
    oculta = obtener_palabra()
    errores = 0
    faltan = len(oculta)

    while errores < 7:
        letra = raw_input("Letra: ")
        if letra not in introducidas:
            introducidas = introducidas + letra
        else:
            print 'letra repe'
            continue
        # control de errrores
        if letra not in oculta:
            errores = errores + 1
        faltan = muestra_resultado(oculta, introducidas, errores)
        if faltan == 0:
            print "\n      Has ganado"
            break

        
if __name__ == '__main__':
    main()
        
        
    
