"""
Pide un año
Informa de si el año es bisiesto o no
"""

def bisiesto_1(year):
    """
    Calcula años bisisestos

    >>> bisiesto_1(1900)
    False
    >>> bisiesto_1(2000)
    True
    >>> bisiesto_1(1992)
    True
    >>> bisiesto_1(2007)
    False
    """
    if year % 4 == 0:
        return True
    else:
        return False

def bisiesto_2(year):
    """
    Calcula años bisisestos

    >>> bisiesto_2(1900)
    False
    >>> bisiesto_2(2000)
    True
    >>> bisiesto_2(1992)
    True
    >>> bisiesto_2(2007)
    False
    """
    mul = year % 100
    mul2 = year % 400
    mul3 = year % 4
    if (mul3 == 0 and mul != 0) or mul2 == 0: # (mul3 == 0 and mul == 0 and mul2 == 0):
        return True
    else:
        return False

def bisiesto_pablo(year):
    """
    Calcula años bisisestos

    >>> bisiesto_pablo(1900)
    False
    >>> bisiesto_pablo(2000)
    True
    >>> bisiesto_pablo(1992)
    True
    >>> bisiesto_pablo(2007)
    False
    """
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    return False

def bisiesto_ad(year):
    """
    Calcula años bisisestos

    >>> bisiesto_ad(1900)
    False
    >>> bisiesto_ad(2000)
    True
    >>> bisiesto_ad(1992)
    True
    >>> bisiesto_ad(2007)
    False
    """
    if year % 400 == 0 or (year % 4 == 0 and year % 100 !=0):
        return True
    else:
        return False
        


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
        




















    
    
