# Búsqueda binaria #
  * http://es.wikipedia.org/wiki/Algoritmo_de_b%C3%BAsqueda
## Algoritmo ##
```
def binary_search(v, L):
    """Devuelve el índice de la primera ocurrencia de v en la lista L
    o -1 si v no está en L."""

    # Marca los índices izquierda y derecah de la seccion.
    i = 0
    j = len(L) - 1
    
    while i != j + 1:
        m = (i + j) / 2
        if L[m] < v:
            i = m + 1
        else:
            j = m - 1

    if 0 <= i < len(L) and L[i] == v:
        return i
    else:
        return -1
```

## Test ##
```
import nose
from binary_search import binary_search

# The list to search with.
VALUES = [1, 3, 4, 4, 5, 7, 9, 10]

def test_first():
    '''Test a value at the beginning of the list.'''
    assert binary_search(1, VALUES) == 0

def test_duplicate():
    '''Test a duplicate value.'''
    assert binary_search(4, VALUES) == 2

def test_middle():
    '''Test searching for the middle value.'''
    assert binary_search(5, VALUES) == 4

def test_last():
    '''Test searching for the last value.'''
    assert binary_search(10, VALUES) == 7

def test_missing_start():
    '''Test searching for a missing value at the start.'''
    assert binary_search(-3, VALUES) == -1

def test_missing_middle():
    '''Test searching for a missing value in the middle.'''
    assert binary_search(2, VALUES) == -1

def test_missing_end():
    '''Test searching for a missing value at the end.'''
    assert binary_search(11, VALUES) == -1

if __name__ == '__main__':
    nose.runmodule()
```