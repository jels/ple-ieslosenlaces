# -*- coding: utf-8 -*-

"""
Explicación de lo que hace el programa
Explicación de cómo se utiliza
Datos de desarrollo y versiones
"""

def pide_fichero():
    """
    pide_fichero() devuelve nombre del fichero 
    
    Devuelve el nombre del fichero que introduce el usuario
    """
    nombre = raw_input("Escribe el nombre del fichero: ")
    return nombre

def abre_fichero(nom_fich):
    """
    abre_fichero(nomb_fich) abre nom_fich en modo lectura y devuelve el 
    objeto fichero
    """
    return open(nom_fich)

def suma_fichero(f):
    """
    suma_fichero(f) devuelve la suma de los número del fichero de texto 
    ... f
    """
    total = 0
    for l in f:
        total = total + float(l)   # importante convertir línea (str) a float
        #f.close()  # cierra el fichero f
    return total  # Importante return fuera del for ...


def muestra_mensaje(nombre_f, suma):
    """
    muestra_mensaje imprime el mensaje al usuario
    """
    print "El fichero", nombre_f, 'tiene unos gastos de', suma
    

def main():
    """
    Función principal que llama al resto ...
    """
    nombre = pide_fichero()
    f = abre_fichero(nombre)
    suma_total = suma_fichero(f)
    f.close()
    muestra_mensaje(nombre, suma_total)
    
    
    
if __name__ == '__main__':
    main()
    

    

    
    