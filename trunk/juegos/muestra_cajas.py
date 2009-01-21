import pygame
import sys
from pygame.locals import *
from cajas import Caja, CajaArribaAbajo

pygame.init()
screen = pygame.display.set_mode([150, 150])
cajas = []
for color, posicion in [
    ([255,0,0], [0,0]),
    ([0,255,0], [0,60]),
    ([0,0,255], [0,120])
    ]:
    cajas.append(CajaArribaAbajo(color, posicion))

    
en_marcha = True
while en_marcha:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            en_marcha = False
    # limpiar pantalla
    screen.fill([0,0,0])
    for c in cajas:
        c.update(150, 150)
        screen.blit(c.image, c.rect)
    pygame.display.update()
    pygame.time.delay(10)

    

