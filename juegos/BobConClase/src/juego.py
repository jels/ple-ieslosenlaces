# -*- encoding: utf-8 -*-
'''
Created on 24/11/2009

@author: lm
'''

import pygame
from pygame.locals import *
from auxiliar import *
from personajes import *
import os
from sys import exit

# inicializar pygame
pygame.init()

ANCHO, ALTO = 400, 300

screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Cangriburguer ñam ñam')

# preparar recursos
# fondo
ruta_imagen_fondo = os.path.join('datos', 'bikini.jpg')
fondo, f_rect = cargar_imagen(ruta_imagen_fondo)
#personajes
bob1 = Bob()
bob2 = Bob()
ham = Hamburguesa()

pygame.mixer.music.load(os.path.join('datos', 'bob.mp3'))
pygame.mixer.music.play(-1)

# posición inicial

bob1.mueve(screen, (30, 0))
bob2.mueve(screen, (30, 150))
                   
lista_hamburguesas = []                        
# Bucle infinito del juego
contador = 0
while True:
    pygame.time.delay(10)
    # Captura de eventos y reacciones
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                dx = -1
            if event.key == K_RIGHT:
                dx = 1
        if event.type == KEYUP:
            dx = 0
    # ham
    if contador % 100 == 0:
        lista_hamburguesas.append(Hamburguesa())
    contador +=1
    # preparo fondo
    screen.blit(fondo, (0,0))
    # calculo movimiento
    bob1.desplaza(screen, (0, 1))
    bob2.desplaza(screen, (1, 0))
    bob1.comprueba_choque(bob2)
    for ham in lista_hamburguesas:
        if not ham.chof:
            ham.mueve(screen)
        ham.dibuja(screen)
                
    pygame.display.update()