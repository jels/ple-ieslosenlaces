# -*- encoding: utf-8 -*-
"""
Basado en http://www.purplestatic.com/gs/pdf/invaders.pdf
"""

import os, sys
import pygame
from pygame.locals import *

def load_image(name):
    fullname = os.path.join('data',name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'cannot load image: ', name
        raise SystemExit, message
    image = image.convert()
    colorkey = image.get_at((0,0))
    image.set_colorkey(colorkey,RLEACCEL)
    return image
def main():
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption('Invasores del espacio')
    sky = pygame.image.load('data/sky.bmp')
    winScreen = pygame.image.load('data/winner.bmp')
    alien = load_image('alien.bmp')
    ship = load_image('ship.bmp')
    bullet = load_image('bullet.bmp')
    pygame.mouse.set_visible(0)
    ships = [ [1,1,1,1], [1,1,1,1], [1,1,1,1] ]
    shipsCount = 12
    shipsX = 10
    shipsY = 10
    shipDir = 1
    bulletX = 320
    bulletY = -10
    while (1):
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == MOUSEBUTTONDOWN:
                bulletY = 420
                pos = pygame.mouse.get_pos()
                bulletX = (pos[0]+25)
        if shipsCount > 0:
            screen.blit(sky,(0,0))
            for j in range(3):
                for i in range(4):
                    if ships[j][i]:
                        screen.blit(alien,((i*40+shipsX),(j*40+shipsY)))
            shipsX += 2 * shipDir
            if shipsX > 400 or shipsX < 10:
                shipDir *= -1
                shipsY += 40
            pos = pygame.mouse.get_pos()
            screen.blit(bullet,(bulletX,bulletY))
            screen.blit(ship,(pos[0],420))
            bulletY -= 5
            if bulletX > shipsX and bulletX < (shipsX + 150):
                if bulletY > shipsY and bulletY < (shipsY + 110):
                    tempY = bulletX - shipsX
                    tempY /= 40
                    if ships[2][tempY]:
                        ships[2][tempY] = 0
                        bulletY = -10
                        shipsCount -= 1
                    elif ships[1][tempY]:
                        ships[1][tempY] = 0
                        bulletY = -10
                        shipsCount -= 1
                    elif ships[0][tempY]:
                        ships[0][tempY] = 0
                        bulletY = -10
                        shipsCount -= 1
            pygame.display.flip()
        else:
            screen.blit(winScreen,(0,0))
            pygame.display.flip()
if __name__ == "__main__": main()
