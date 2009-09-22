# -*- coding: cp1252 -*-

# importar m�dulos
import pygame
from pygame.locals import *
import sys
import os
from auxiliar_juegos import *




class Mano(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = cargar_imagen('mano.bmp', -1)
        self.golpea = False
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        if self.golpea:
            self.rect.move_ip(5,10)
    def baja(self, destino):
        """Devuelve verdadero si la mano golpea al mono
        """
        if not self.golpea:
            self.golpea = True
            area_toque = self.rect.inflate(-5, -5)
            return area_toque.colliderect(destino.rect)
    def levanta(self):
        self.golpea = False
    

class Mono(pygame.sprite.Sprite):
    def __init__(self, vel=6):
        # inicializa objeto tipy Sprite
        pygame.sprite.Sprite.__init__(self)
        # carga la imagen: devuelve imagen y rect�ngulo
        self.image, self.rect = cargar_imagen('chimp.bmp', -1)
        ventana = pygame.display.get_surface()
        self.area = ventana.get_rect()
        self.rect.topleft = 10, 10
        #ventana.blit(self.imagen, (0,0))
        self.move = vel
        self.ruido_choca = cargar_sonido('punch.wav')
        self.vidas = 3
        self.vueltas = 0 # contador de vueltas
        self.aciertos = 0
    def _anda(self):
        nueva_pos = self.rect.move((self.move, 0))
        if self.rect.left < self.area.left or \
            self.rect.right > self.area.right:
            # activa contador de vueltas
            self.vueltas = self.vueltas + 1
            print '-->', self.vueltas
            self.ruido_choca.play()
            self.move = -self.move
            nueva_pos = self.rect.move((self.move, 0))
            self.image = pygame.transform.flip(self.image, 1, 0)
            
        self.rect = nueva_pos
    def update(self):
        self._anda()
    def tocado(self):
        """ Qu� tiene que hacer si es golpeado"""
        self.vidas = self.vidas - 1
        print "-->>>> vidas:", self.vidas
        self._cambia_mono()
        if self.vidas == 0:
            self.kill()
    def _cambia_mono(self):
        if self.aciertos == 1:
            self.image, self.rect = cargar_imagen('chimp2.bmp', -1)
        else:
            self.image, self.rect = cargar_imagen('chimp3.bmp', -1)
        if self.move > 0:
            self.move = self.move + 2
        else:
            self.move = self.move - 2
        
        

def main():
    # inicializar pygame
    pygame.init()
    # configurar la pantalla
    ventana = pygame.display.set_mode((600, 60))  # resoluci�n (,)
    pygame.display.set_caption("Juego del mono")  # t�tulo ventana
    pygame.mouse.set_visible(0)  # oculta punter rat�n

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
    #mono2 = Mono(10)
    #mono3 = Mono(4)
    mano = Mano()
    personajes = pygame.sprite.RenderPlain((mono, mano)) #,mono2,mono3))

    # texto
    vidas = "Vidas: %d"
    fuente = pygame.font.SysFont("arial", 24)
    rojo = pygame.color.Color('red')
    gris = pygame.color.Color('grey')

    en_juego = True
    # terminar?
    while True:
        reloj.tick(100)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if en_juego:
                if event.type == MOUSEBUTTONDOWN:
                    if mano.baja(mono):
                        print "Tocado"
                        mono.tocado()
                        if mono.vidas == 0:
                            en_juego = False
                            vidas = "Game Over  (%d)"
                            fuente = pygame.font.SysFont("arial", 64)
                elif event.type == MOUSEBUTTONUP:
                    mano.levanta()
		
	personajes.update()
	
	#Vuelvo a dibujar todo 
	screen.blit(fondo, (0,0))
	vidas_surface = fuente.render(vidas % mono.vidas, True, rojo, gris)
	screen.blit(vidas_surface, (0,0))
	personajes.draw(screen)
	pygame.display.flip()

               
if __name__ == '__main__':
    main()