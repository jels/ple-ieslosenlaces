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
    
    
