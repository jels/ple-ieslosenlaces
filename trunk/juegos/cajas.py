# -*- encoding: utf-8 -*-

import pygame

"""
Ejemplos sprites: imagen + posición
"""

class Caja(pygame.sprite.Sprite):
    def __init__(self, color, posicion_inicial):
        # Llamada al init del padre
        pygame.sprite.Sprite.__init__(self)
        # creamos la imagen y rellenamos con color
        self.image = pygame.Surface([15,15])
        self.image.fill(color)
        # colocar en pantalla
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion_inicial
        
    
    
