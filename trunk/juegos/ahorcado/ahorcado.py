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