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
        # dimensiones pantalla
        self.ventana = pygame.display.get_surface()
        self.ancho = self.ventana.get_width()
        self.alto = self.ventana.get_height() 
        self.rect.bottomleft = (0, self.alto - 5)
        # control de movimientos
        self.derecha = False
        self.izquierda = False
    def update(self):
        if self.izquierda == True:
            if self.rect.left > 0:
                self.rect.left -= 1
            else:
                self.izquierda = False
        if self.derecha == True:
            if self.rect.right < self.ancho:
                self.rect.right += 1
            else:
                self.derecha = False
                
    def dispara(self):
        misil = Disparo(self.rect.midtop)
        return misil
             
                
                
class Enemigo(pygame.sprite.Sprite):
    # Variables de clase
    izquierda = False # indica direccion de movimiento
    toca_izquierda = False # variable centinela: avisa
    altura = 0
    def __init__(self, pos_inicial):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = cargar_imagen('malo.png')
        self.rect.topleft = pos_inicial
        self.ypos = pos_inicial[1]
        self.ventana = pygame.display.get_surface()
        self.ancho = self.ventana.get_width()
    def update(self):
        if self.rect.left <= 0:
            Enemigo.toca_izquierda = False
            
        elif self.rect.right >= self.ancho:  #OJO
            Enemigo.toca_izquierda = True
            
        if Enemigo.izquierda == True:
            self.rect.left -= 1
        else:
            self.rect.left += 1
        
        self.rect.topleft = [self.rect.topleft[0],
                             Enemigo.altura+self.ypos]
    def direccion():
        if Enemigo.izquierda != Enemigo.toca_izquierda:
            Enemigo.altura += 10
            Enemigo.izquierda = Enemigo.toca_izquierda
    direccion = staticmethod(direccion)
        
    
        

class Disparo(pygame.sprite.Sprite):
    def __init__(self, pos_inicial):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = cargar_imagen('disparo.png', -1)
        self.rect.topleft = pos_inicial
        self.vivo = True
    def update(self):
        if self.rect.top > 0:
            self.rect.top -= 1
            return True
        else:
            self.kill()
            self.vivo = False
    def toca_nave(self, naves):
        if pygame.sprite.spritecollide(self,naves, True):
            return True
        else:
            return False
            
        