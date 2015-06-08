# ¿Qué sabemos hacer? #

## Números ##
  * Operaciones con enteros y números reales
  * Uso de math
```
import math
math.sqrt(9)
```
  * Uso de variables
```
nombre = "Pilar"
edad = 19
```
  * ucles para repeticiones fijas
```
# repite 10 veces algo
for x in range(10)
    print x
```
## Cadenas de caracteres ##
  * Crear, concatenar, recorrer, trocear
```
for letra in cadena:
    print letra
```

```
datos = "nombre; edad; salario"
for d in datos.split(';'):
    print d
```
```
nombre = 'Juan'
apellido = 'Pérez'
nombre_completo = nombre + ' ' + apellido
```

## Estructuras de control ##
```
if edad < 18:
    print 'Menor de edad'
else:
    print 'Mayor de edad'
```
contador = 1
limite = 10
```
{{{
}}}
while contador <= limite:
    print contador
    contador += 1
```
```
for x in range(10, 0, -1):
    print x
```
## Ficheros ##
```
fich_lectura = open('datos.txt')
for linea in fichero:
    print linea
```
```
fich_escritura = open('datos.txt', 'w')
fich_escritura.write(nombre + ';' + str(edad) + '\n')
```

## Funciones ##
```
def mayor_de_edad(edad):
    if edad < 18:
        return False
    else:
        return True
mayor_de_edad(24)
```

## Listas ##
```
for elemento in lista:
    print elemento

primero = lista[0]
ultimo = lista[-1]
tres_primeros = lista[0:3]
lista.append(nuevo_elemento)
clon_de_lista = lista[:]
if elemento in lista:
   print 'Sí que está'
```

```
notas_alumnos = [[5,7,4,8],
                 [6,8,4,3],
                 [7,8,9,7]]
print 'Notas primer alumno'
for x in notas_alumnos[0]:
    print x
print 'Notas primer ejercicio'
for al in notas_alumnos:
    print al[0]
print 'todas las notas'
for al in notas_alumnos:
    for nota in al:
        print nota,
    print
```