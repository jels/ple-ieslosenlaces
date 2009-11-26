# -*- encoding: utf-8 -*-
'''
Created on 26/11/2009

@author: lm

Archivo para importar desde nuestros juego
Sólo tendrá definiciones ...
'''
import pygame
from pygame.locals import *

# Función para cargar imágenes
def cargar_imagen(ruta, colorkey = None):
    """cargar_imagen(ruta, ...)  --> devuelve imagen y rectángulo
    """
    try:
        imagen = pygame.image.load(ruta)
    except pygame.error, mensaje:
        print 'No se puede cargar la imagen', ruta
        raise SystemExit, mensaje
    if colorkey is not None:
        imagen = imagen.convert()
        if colorkey is -1:
            colorkey = imagen.get_at((0,0))
        imagen.set_colorkey(colorkey, RLEACCEL)
    else:
        if imagen.get_alpha() is None:
            imagen = imagen.convert()
        else:
            imagen = imagen.convert_alpha()
    return imagen, imagen.get_rect()