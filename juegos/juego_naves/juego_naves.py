#-*- encoding: utf-8 -*-

import pygame
from pygame.locals import *
from auxiliar import *
import sys


pygame.init()

# variables globales
ALTO, ANCHO = 480, 320


screen = pygame.display.set_mode([ANCHO, ALTO])  # Tamaño de la pantalla

# creación de objetos
minave = Nave()
lista_naves = pygame.sprite.Group()
disparos = pygame.sprite.Group()
for x in range(6):
    for y in range(0, ALTO/3, 30):
        lista_naves.add(Enemigo((x*40+10,y+10)))

# bucle principal del juego
while True:
    screen.fill([0,0,0])
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
            elif event.key == K_SPACE: 
                disparos.add(minave.dispara())

    # actualiza minave
    minave.update()
    screen.blit(minave.image, minave.rect)
    
    # actualiza lista_naves
    lista_naves.update()
    lista_naves.draw(screen)

    # actualiza disparos    
    disparos.update()
    disparos.draw(screen)
    
    for disparo in disparos:
        if disparo.toca_nave(lista_naves):
            disparos.remove(disparo)
    Enemigo.direccion()
                
    pygame.display.update()
    pygame.time.delay(10)
