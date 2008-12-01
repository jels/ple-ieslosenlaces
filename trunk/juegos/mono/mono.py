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
        self.image, self.rect = cargar_imagen('chimp.bmp', -1)
        ventana = pygame.display.get_surface()
        self.area = ventana.get_rect()
        self.rect.topleft = 10, 10
        #ventana.blit(self.imagen, (0,0))
        self.move = 6
        self.ruido_choca = cargar_sonido('punch.wav')
    def _anda(self):
        nueva_pos = self.rect.move((self.move, 0))
        if self.rect.left < self.area.left or \
            self.rect.right > self.area.right:
            self.ruido_choca.play()
            self.move = -self.move
            nueva_pos = self.rect.move((self.move, 0))
            self.image = pygame.transform.flip(self.image, 1, 0)
        self.rect = nueva_pos
    def update(self):
        self._anda()
        

def main():
    # inicializar pygame
    pygame.init()
    # configurar la pantalla
    ventana = pygame.display.set_mode((600, 60))  # resoluci�n (,)
    pygame.display.set_caption("Juego del mono")  # t�tulo ventana

    screen = pygame.display.get_surface()

    # fondo
    fondo = pygame.Surface(screen.get_size())
    fondo = fondo.convert() 
    fondo.fill((0, 250, 0))
    


    # dibujar
    screen.blit(fondo, (0,0))
    pygame.display.flip()

    # crear personajes
    reloj = pygame.time.Clock()  # reloj que controla movimientos
    mono = Mono()
    personajes = pygame.sprite.RenderPlain((mono))

    # terminar?
    while True:
        reloj.tick(100)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
                
        personajes.update()
        
        #Vuelvo a dibujar todo 
        screen.blit(fondo, (0,0))
        personajes.draw(screen)
        pygame.display.flip()

               
if __name__ == '__main__':
    main()
