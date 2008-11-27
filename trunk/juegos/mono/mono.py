# -*- coding: cp1252 -*-

# importar módulos
import pygame
from pygame.locals import *
import sys
import os

# inicializar pygame
pygame.init()

# configurar la pantalla
ventana = pygame.display.set_mode((480, 160))  # resolución (,)
pygame.display.set_caption("Juego del mono")  # título ventana
screen = pygame.display.get_surface()


# fondo
fondo = pygame.Surface(screen.get_size())
fondo = fondo.convert()
fondo.fill((0, 250, 0))
screen.blit(fondo, (0, 0) )

# poner imagen
fichero_mono = os.path.join('data', 'chimp.bmp')
imagen_mono = pygame.image.load(fichero_mono)
screen.blit(imagen_mono, (0,0) )


# refrescar pantalla
pygame.display.flip()


avanza_x = 1
posx = 0
posy = 0

# terminar?
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                posx = posx -10
            if event.key == K_RIGHT:
                posx = posx +10
            if event.key == K_UP:
                posy = posy -10
            if event.key == K_DOWN:
                posy = posy +10
            # fondo y mono
            screen.blit(fondo, (0, 0))
            screen.blit(imagen_mono, (posx, posy) )
            pygame.display.flip()   
        
    """
    movimiento automático
    if posx > 470 or posx < 1:
        avanza_x = avanza_x * -1

    posx = posx + avanza_x
    
    screen.blit(imagen_mono, (posx,0) )
    pygame.display.flip()
    """
    #pygame.time.delay(10)
            
            
            
            


