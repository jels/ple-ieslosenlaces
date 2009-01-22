#-*- encoding: utf-8 -*-

import pygame
from pygame.locals import *
from auxiliar import *
import sys



pygame.init()

# variables globales
ALTO, ANCHO = 240, 320


screen = pygame.display.set_mode([ALTO, ANCHO])  # Tamaño de la pantalla

minave = Nave()


# bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                minave.derecha = True
                minave.izquierda = False
            elif event.key == K_LEFT:
                minave.derecha = False
                minave.izquierda = True

    minave.update()
    screen.blit(minave.image, minave.rect)
    pygame.display.update()
    pygame.time.delay(10)
