## Llamada a funciones ##
Cuando Python llega a una llamada a una función, inicia un proceso de cuatro pasos:
  1. El programa que hace la llamada suspende su ejecución en el punto de la llamada.
  1. Los parámetros formales de la función reciben los valores de la llamada actual
  1. Se ejecuta el cuerpo de la función
  1. Se devuelve el control al punto siguiente de la llamada a la función.

## Funciones que modifican parámetros ##
  * Para devolver información de dentro de la función al programa que la ha llado usamos _return_
  * Las funciones también pueden comunicarse modificando parámetros (parámetros de entrada y salida)
```
def suma_edad(edad):
    edad = edad +1

edad = 18
suma_edad(edad)
print edad
```

## Funciones y estructura de los programas ##
  * Funciones como mecanismos para reducir al duplicación del código
  * Romper la complejidad de un programa en subprogramas más pequeños.
