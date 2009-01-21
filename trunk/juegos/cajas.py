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
        
class CajaArribaAbajo(pygame.sprite.Sprite):
    def __init__(self, color, posicion_inicial):
        # Llamada al init del padre
        pygame.sprite.Sprite.__init__(self)
        # creamos la imagen y rellenamos con color
        self.image = pygame.Surface([15,15])
        self.image.fill(color)
        # colocar en pantalla
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion_inicial
        self.hacia_abajo = True
        self.hacia_derecha = True
    def update(self, bajo, ancho):
        if self.rect.bottom == bajo - 1:
            self.hacia_abajo = False
        elif self.rect.top == 0:
            self.hacia_abajo = True
        if self.rect.right == ancho - 1:
            self.hacia_derecha = False
        elif self.rect.left == 0:
            self.hacia_derecha = True
        if self.hacia_abajo:
            self.rect.top += 1
        else:
            self.rect.top -= 1
        if self.hacia_derecha:
            self.rect.left += 1
        else:
            self.rect.left -= 1


    
        
    
    








