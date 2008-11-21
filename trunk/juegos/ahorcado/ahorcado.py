#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import os
import sys

pygame.init()

screen = pygame.display.set_mode((350, 300))
pygame.display.set_caption("Juego ahorcado")

#### poner sonido
sonido = pygame.mixer.Sound(
    os.path.join('data', 'telefono.ogg'))
sonido.play()


#### poner texto
fuente = pygame.font.Font(None, 48)
texto = fuente.render("_ _ _ _ _ _ _",1 , (10, 10, 10))
posicion_texto = texto.get_rect()
posicion_texto.centerx = screen.get_rect().centerx
posicion_texto.centery = 280


num = 0 ## repeticiones --> nombres de imágenes

while True:
    
    events = pygame.event.get()
    for event in events:
        #print event
        if event.type == QUIT:
            sys.exit(0)
    fondo = pygame.image.load(
        os.path.join('data', '%d.jpg' % (num%8)))

    fondo = fondo.convert()

    screen.blit(fondo, (0,0))
    
    screen.blit(texto, posicion_texto)
    pygame.display.flip()

    num = num + 1
    #sonido.play()
    pygame.time.delay(4000) # 1 segundo de retardo

            

import pygame
from pygame.locals import *
import os

pygame.init()
screen = pygame.display.set_mode((350, 300))
pygame.display.set_caption("Juego ahorcado")

for x in range(8):
    fondo = pygame.image.load(os.path.join('data', '%d.jpg' % x))
    fondo = fondo.convert()
    screen.blit(fondo, (0,0))
    pygame.display.flip()
    pygame.time.delay(1000)


raw_input()
