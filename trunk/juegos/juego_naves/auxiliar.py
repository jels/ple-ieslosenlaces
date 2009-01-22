#-*- encoding: utf-8 -*-

import os
import pygame
from pygame.locals import *

def cargar_imagen(nombre, colorkey=None):
    ruta = os.path.join('data', nombre)
    try:
        imagen = pygame.image.load(ruta)
    except pygame.error, mensaje:
        print "Error al cargar la imagen", ruta
        raise SystemExit, mensaje
    imagen = imagen.convert() # convierte la imagen al modo usado
    if colorkey is not None:
        if colorkey == -1:
            colorkey = imagen.get_at((0, 0))
        imagen.set_colorkey(colorkey, RLEACCEL)
    return imagen,  imagen.get_rect()

def cargar_sonido(nombre):
    ruta = os.path.join('data', nombre)
    try:
        sonido = pygame.mixer.Sound(ruta)
    except pygame.error, mensaje:
        print 'No puede cargar sonido', ruta
        raise SystemExit, mensaje
    return sonido
    

class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = cargar_imagen('nave.png', -1)
        #dimensiones pantalla
        sf = pygame.display.get_surface()
        pos_y = sf.get_height()
        # posición inicial
        self.rect.bottomleft = [0,  pos_y -5 ]
        #max ancho = pantalla
        self.max_ancho = sf.get_width()
        # control movimiento
        self.derecha = False
        self.izquierda = False
        self.misiles = []
    def update(self):
        if self.izquierda == True:
            if self.rect.left > 0:
                self.rect.left -= 1 
            else:
                self.izquierda = False
        if self.derecha == True:
            if self.rect.right < self.max_ancho:
                self.rect.left += 1
            else:
                self.derecha = False
        for m in self.misiles:
            m.update()
    def dispara(self):
        self.misiles.append(Disparo(self.rect.midtop))       
        
        
            
       
       
        
class Enemigo(pygame.sprite.Sprite):
    izquierda = False
    altura = 0
    def __init__(self, pos_inicial):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = cargar_imagen('malo.png')
        self.rect.topleft = pos_inicial
        self.ypos = pos_inicial[1]
    def update(self, ancho):
        if self.rect.topleft[0] == 0:
            Enemigo.izquierda = False
            Enemigo.altura += 1
            self.altura += 1
        elif self.rect.topright[0] == ancho:  #OJO
            Enemigo.izquierda = True
            Enemigo.altura += 1
        if Enemigo.izquierda == True:
            self.rect.topleft = [self.rect.topleft[0]-1, \
                                 self.rect.topleft[1]]
        else:
            self.rect.topleft = [self.rect.topleft[0]+1, \
                                 self.rect.topleft[1]]
        self.rect.topleft = [self.rect.topleft[0],
                             Enemigo.altura+self.ypos]
        
class Disparo(pygame.sprite.Sprite):
    def __init__(self, pos_inicial):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = cargar_imagen('disparo.png')
        self.rect.topleft = pos_inicial
        self.vivo = True
    def update(self):
        if self.rect.top > 0:
            self.rect.top -= 1
        else:
            self.kill()
            #self.vivo = False
    def toca_nave(self, naves):
        for nave in pygame.sprite.spritecollide(self,naves, 0):
            nave.kill()
            self.kill()
    
        
            
def comprueba_colisiones(nave, enemigos):
    for m in nave.misiles:
        m.toca_nave(enemigos)

            
        
            
            
        
    
        
        
        
        
        
        
        
        
        
        
        

            
            
            