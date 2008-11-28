import os
import pygame

def cargar_imagen(nombre, colorkey=None):
    ruta = os.path.join('data', nombre)
    try:
        imagen = pygame.image.load(ruta)
    except pygame.error, mensaje:
        print "Error al cargar la imagen", ruta
        raise SystemExit, mensaje
    return imagen #, imagen.get_rect()
    
    
