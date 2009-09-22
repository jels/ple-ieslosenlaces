# -*- coding: utf-8 -*-

import sys, pygame
from pygame.locals import *
import random

"""
Parte de la introducción a pygame de 
http://www.losersjuegos.com.ar/referencia/articulos/pygame_intro/pygame_intro.php
"""

#### Definición de clases
class Pelota(object):
    def __init__(self, tam, color):
        """
        Crea pelota de tamaño (diámetro) y color
        """
        self.tam = tam
        self.color = color
        self.rect = pygame.Rect(0,0,self.tam, self.tam)
        self.paso = random.randint(1,3)
        self.velocidad = [self.paso, self.paso]
    def muevete(self):
        self.rect = self.rect.move(self.velocidad)
        if self.rect.left < 0 or self.rect.right > 320:
            self.velocidad[0] = self.velocidad[0] * -1
        if self.rect.top < 0 or self.rect.bottom > 240:
            self.velocidad[1] = self.velocidad[1] * -1
    def centro(self):
        """Devuelve las coordenadas del centro"""
        return self.rect.center
    
        
    
pygame.init()

size = width, height = 640, 480 #320, 240

black = 0, 0, 0

screen = pygame.display.set_mode(size)

# crear rectángulo de 10x10
#p1 = Pelota(10, (255,255,255))
#p2 = Pelota(20, (255,0, 0))
#p3 = Pelota(30, (0,255, 0))
lista_tams = [5, 10, 20, 30]
lista_colors = [(255,255,255)]

lista_pelotas = []

while 1:
    
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            lista_pelotas.append(Pelota(random.randint(5,30),
                                        (random.randint(0,255),
                                         random.randint(0,255),
                                         random.randint(0,255)
                                         )
                                        )
                                 )
            
    
    for p in lista_pelotas:
        p.muevete()
    

    screen.fill(black)
    for p in lista_pelotas:
        pygame.draw.circle(screen, p.color , p.centro(), p.tam)

    pygame.display.flip()
    pygame.time.delay(10)

