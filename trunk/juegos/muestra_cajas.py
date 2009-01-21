import pygame
import sys
from pygame.locals import *
from cajas import Caja

pygame.init()
screen = pygame.display.set_mode([150, 150])
cajas = []
for color, posicion in [
    ([255,0,0], [0,0]),
    ([0,255,0], [0,60]),
    ([0,0,255], [0,120])
    ]:
    cajas.append(Caja(color, posicion))
for c in cajas:
    screen.blit(c.image, c.rect)
    
pygame.display.update()

en_marcha = True
while en_marcha:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            en_marcha = False
    

