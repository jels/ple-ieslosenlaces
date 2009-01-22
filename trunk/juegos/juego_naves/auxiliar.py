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
            
        
        
    
        

        
        
class Enemigo(pygame.sprite.Sprite):
    def __init__(self, pos_inicial):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = cargar_imagen('malo.png')
        self.rect.topleft = pos_inicial
    def update(self):
        pass
        
    
        
        
        
        
        
        
        
        
        
        
        
