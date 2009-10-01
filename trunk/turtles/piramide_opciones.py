# -*- coding: cp1252 -*-
# Piramide con opciones
from turtle import *
import random

# Ocultar tortuguita
screen = Screen()
screen.tracer(1, 0)
ht()

# Situarse más a la izquierda y abajo
up()
goto(-200, -100)
down()

# Pedimos la altura que quiere que tenga el cubito
alt = input("Altura del cubito: ")

# Función que dibuja un cubito
def cubito():
    up()
    fd(alt)
    lt(90)
    down()
    for x in range (4):
        fd(alt)
        lt(90)
    rt(90)

# Pedimos el numero de lineas que quiere que tenga la piramide
n = input("¿De cuantas alturas la quieres?: ")

# Variables
altura = alt        # Distancia que tendrá que subir la tortuga para cada línea
longitud = alt/2    # Distancia de diferencia de inicio en cada fila

# Función que dibuja una fila de n cubitos
def fila_cubitos(n):
    y = 0           # Inicializamos a 0 para que en cada vuelta entre en el siguiente for
    for y in range(n):
        colores = ["red", "yellow", "orange", "green", "cyan", "grey", "brown", "purple", "black", "violet", "azure", "chartreuse",
                   "#DFFF00", "#EC3B83", "#CD00CC", "#50C878", "#FF00FF", "#ADFF2F", "#F400A1", "blue", "navy"]     # Colores a elegir
        random.shuffle(colores)     # Mezclamos los colores
        color("black",colores[1])   # Elegimos el primero
        begin_fill()                # Dibujamos el cubito y lo rellenamos
        cubito()
        end_fill()

# Función que dibuja la piramide de n alturas
for x in range(n):
    fila_cubitos(n)                 # Dibujamos cada fila de cubitos
    up()                            # Alzamos el lápiz
    goto(-200, -100)                # Nos volvemos a colocar en el inicio
    lt(90)                          # Giramos el cursor
    fd(altura)                      # Para posteriormente subir
    altura += alt                   # Incrementamos el valor de la altura para el siguiente nivel
    rt(90)                          # Para colocarnos para seguir dibujando otra línea
    fd(longitud)
    longitud += alt/2               # Incrementamos el valor de la longitud para la próxima fila
    n -= 1                          # Reducimos la n, para que en cada fila dibuje un cubito menos
    down()                          # Volvemos a colocar el lápiz en situación de dibujar
