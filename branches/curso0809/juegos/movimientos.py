# -*- coding: utf-8 -*-
 
import sys, pygame
from pygame.locals import *
import random
 
 
#### Definición de clases
class Objeto(object):
    def __init__(self, x, y):
        """
        Crea objeto en pos de ratón
        """
        self.tam = 20
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(x,y, 40, 40)
        self.paso = random.randint(1,3)
        self.velocidad = [self.paso, self.paso]
        self.rect.center = (x,y)
        self.select = False
    def muevete(self, x,y):
        self.rect = self.rect.move(x,y)
    def tocado(self, x, y):
        return self.rect.collidepoint(x, y)
    def centro(self):
        return self.rect.center
    def seleccionado(self):
        self.select = True
        self.color = (0,255,0)
    def esta_seleccionado(self):
        return self.select
 
 
pygame.init()
 
size = width, height = 640, 480
 
black = 0, 0, 0
 
screen = pygame.display.set_mode(size)
 
lista_objetos = []
 
while 1:
 
    for event in pygame.event.get():
 
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            tocado = False
            for cosa in lista_objetos:
                if cosa.tocado(pos[0], pos[1]):
                    cosa.seleccionado()
                    tocado = True
                    break
            if not tocado:
                lista_objetos.append(Objeto(pos[0], pos[1]))
 
    screen.fill(black)
    for p in lista_objetos:
        pygame.draw.circle(screen, p.color , p.centro(), p.tam)
 
    pygame.display.flip()
    pygame.time.delay(10)
