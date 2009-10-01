import pygame
from pygame.locals import *
import sys

from random import *
pygame.init()

screen = pygame.display.set_mode((640, 480), FULLSCREEN)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            # Si pulsa escape tambi�n salimos
            if event.key == K_ESCAPE:
                sys.exit(0)
    random_color = (randint(0, 255), randint(0, 255),randint(0, 255))
    random_pos = (randint(0, 639), randint(0, 479))
    random_radio = randint(1, 200)
    pygame.draw.circle(screen, random_color, random_pos, random_radio)
    pygame.display.update()
    
