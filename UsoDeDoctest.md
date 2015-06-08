# Tests con Doctest #

doctest combina las pruebas con la documentación.

Utiliza las pruebas para comprobar el código y como documentación. Así se suelen mantener pruebas y documentación actualizados.

Cuando doctest encuentra una línea en la documentación que comienza con '>>>' interpreta que lo que le sigue es código Python a ejecutar, y que la respuesta esperada se encuentra en la línea o líneas siguientes, sin >>>. El texto de la prueba termina cuando se encuentra una línea en blanco, o cuando se llega al final de la cadena de documentación.

Ejemplo:
```
# -*- coding: utf-8 -*-

def cuadrado(numero):
    """Calcula el cuadrado de un número

    >>> cuadrado(5)
    25
    >>> cuadrado(10)
    100
    """

    return numero * numero

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
```

Si no pasa las prueba, mostrará el error en pantalla:
```
**********************************************************************
File "/home/lm/Escritorio/ple/prueba_funciones.py", line 6, in __main__.cuadrado
Failed example:
    cuadrado(5)
Expected:
    25
Got:
    125
**********************************************************************
File "/home/lm/Escritorio/ple/prueba_funciones.py", line 8, in __main__.cuadrado
Failed example:
    cuadrado(10)
Expected:
    100
Got:
    1000
**********************************************************************
1 items had failures:
   2 of   2 in __main__.cuadrado
***Test Failed*** 2 failures.
```