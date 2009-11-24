# -*- encoding: utf-8 -*-
'''
Created on 24/11/2009

@author: lm
'''

import pygame
from pygame.locals import *
import os
from sys import exit

# inicializar pygame
pygame.init()

ANCHO, ALTO = 400, 300

screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Primer juego')

# preparar recursos
ruta_imagen_fondo = os.path.join('datos', 'bikini.jpg')
ruta_bob = os.path.join('datos', 'bob.png')
fondo = pygame.image.load(ruta_imagen_fondo).convert()
bob = pygame.image.load(ruta_bob).convert_alpha()
dancho = bob.get_width()/2 #desplazamiento ancho
dalto = bob.get_height()/2  # desplaza. alto

pygame.mixer.music.load(os.path.join('datos', 'bob.mp3'))
pygame.mixer.music.play(-1)
                        
x, y = 200, 150
dx, dy = 0, 0
# Bucle infinito del juego
while True:
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
             
    # preparo fondo
    screen.blit(fondo, (0,0))
    # calculo movimiento
    x = x + dx
    
    # ¿dónde está el ratón?
#    x, y = pygame.mouse.get_pos()
#    x = x - dancho
#    y = y - dalto
    # control para que no salga de la pantalla
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if x > ANCHO - 2*dancho:
        x = ANCHO - 2*dancho
    if y > ALTO - 2*dalto:
        y = ALTO - 2*dalto
    screen.blit(bob, (x,y))
    
    pygame.display.update()