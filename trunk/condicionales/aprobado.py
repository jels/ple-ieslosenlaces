def aprobado(nota):
    """
    aprobado(nota) devuelve verdadero si la nota es >= 5
    devuelve falso en caso contrario

    >>> aprobado(5)
    True
    >>> aprobado(4)
    False
    """
    if nota >= 5:
        return True
    if nota < 5:
        return False

def test():
    import doctest
    doctest.testmod()

def main():
    nota = input("Introduzca la nota: ")

    if aprobado(nota):
        print "El alumno está aprobado"
    if not aprobado(nota):
        print "El alumno está suspenso"
        
if __name__ == '__main__':
    #test()
    main()

    
