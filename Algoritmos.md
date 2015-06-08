# Búsqueda #
  * `lista.index(objeto)`
  * Búsqueda binaria: http://code.google.com/p/ple-ieslosenlaces/wiki/BusquedaBinaria

## Ejercicios ##
  1. Encuentra el índice que ocupa el número menor de una serie.
```
def indice_menor(serie):
    '''
    Devuelve el índice que ocupa el valor menor de una serie
    >>> puntos = [3456, 2345, 120, 4590, 43, 23456]
    >>> indice_menor(puntos)
    4
    '''
    pass
```
  1. Encuentra los índices que ocupan los dos números menores de una serie
  1. Una secuencia de ADN es una cadena construida con las siguientes letras: A, T, G, y C. Para encontrar el complemento de una secuencia de ADN las Aes se reemplazan por Tes, las Tes por Aes, las Ges por Ces y las Ces por Ges. Por ejemplo el complemento de AATTGCCGT es TTAACGGCA.
    * Escribe los pasos (en español) para encontrar el complemento.
    * Revisa los pasos. Se cambiará algún carácter al buscar su complemento varias veces?
    * Escribe la función complemento(secuencia) que devuelve el complemento de una secuencia.
  1. Escribe una función minimo\_maximo(secuencia, booleano) Si booleano es True, devuelve el mínimo, si no de vuelve el índice máximo.

**NOTA:** Crea los doctests para todas las funciones antes de empezar a programar. Recuerda http://docs.python.org/library/doctest.html