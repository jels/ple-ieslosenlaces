# -*- encoding: utf-8 -*-

'''
Created on 26/11/2009

@author: lm

módulo con clases de personajes
'''

from auxiliar import *
import os
import random

class Bob(object):
    def __init__(self):
        ruta_bob = os.path.join('datos', 'bob.png')
        self.imagen, self.rect = cargar_imagen(ruta_bob)
        self.dirx = -1
        self.diry = 1
        
    def mueve(self, pantalla, posicion):
        """
        pantalla --> screen 
        posicion --> x, y
        """
        self.rect = pantalla.blit(self.imagen, posicion)
    def desplaza(self, pantalla, (dx, dy)):
        ancho, alto = pantalla.get_size()
        x = self.rect[0]
        y = self.rect[1]
        if x + dx*self.dirx > ancho:
            # corregir dirección
            self.dirx *= -1
            self.gira()
        elif x + dx*self.dirx < 0:
            # corregir dirección
            self.dirx *= -1
            self.gira()
        if y + dy*self.diry > alto:
            # corregir dirección
            self.diry *= -1
            self.voltea()
        elif y + dy*self.diry < 0:
            # corregir dirección
            self.diry *= -1
            self.voltea()
            
        self.mueve(pantalla, (x+dx*self.dirx, y+dy*self.diry))
    def gira(self):
        self.imagen = pygame.transform.flip(self.imagen, True, False)
    def voltea(self):
        self.imagen = pygame.transform.flip(self.imagen, False, True)
    def comprueba_choque(self, otro):
        if self.rect.colliderect(otro.rect):
            self.cambia()
            otro.cambia()
    def cambia(self):
        self.dirx *= -1
        self.diry *= -1
class Hamburguesa(object):
    def __init__(self):
        ruta_ham = os.path.join('datos', 'hamburguesa.png')
        ruta_ham_chof = os.path.join('datos', 'hamburguesa_chof.png')
        self.imagen, self.rect = cargar_imagen(ruta_ham, -1)
        self.imagen_chof, self.rect_chof = cargar_imagen(ruta_ham_chof, -1)
        self.rect[0] = random.randint(0,400)
        self.chof = False
    def dibuja(self, pantalla, posicion=None):
        self.rect = pantalla.blit(self.imagen, self.rect)
    def mueve(self, pantalla):
        self.rect = self.rect.move(0, 1)
        if self.rect[1]>290:
            self.chof = True
            self.imagen = self.imagen_chof
    
        
        
         
        

