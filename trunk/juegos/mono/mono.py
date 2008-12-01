# -*- coding: cp1252 -*-

# importar m�dulos
import pygame
from pygame.locals import *
import sys
import os
from auxiliar_juegos import *


class Mono(pygame.sprite.Sprite):
    def __init__(self):
        # inicializa objeto tipy Sprite
        pygame.sprite.Sprite.__init__(self)
        # carga la imagen: devuelve imagen y rect�ngulo
        self.imagen, self.rect = cargar_imagen('chimp.bmp')
        ventana = pygame.display.get_surface()
        self.area = ventana.get_rect()
        self.rect.topleft = 10, 10
    def _anda(self):
        
        


def main():
    # inicializar pygame
    pygame.init()
    # configurar la pantalla
    ventana = pygame.display.set_mode((480, 60))  # resoluci�n (,)
    pygame.display.set_caption("Juego del mono")  # t�tulo ventana

    screen = pygame.display.get_surface()

    # fondo
    fondo = pygame.Surface(screen.get_size())
    fondo = fondo.convert() 
    fondo.fill((0, 250, 0))
    


    # dibujar
    screen.blit(fondo, (0,0))

    # crear personajes
    mono = Mono()

    
    pygame.display.flip()
    
    
    
    # terminar?
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
   
            
if __name__ == '__main__':
    main()
