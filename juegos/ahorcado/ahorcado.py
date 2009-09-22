#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import os
import sys
import random

pygame.init()
random.seed()

screen = pygame.display.set_mode((350, 300), 0, 16)
pygame.display.set_caption("Juego ahorcado")

#### poner sonido
sonido_mal = pygame.mixer.Sound(
    os.path.join('data', 'mal.wav'))
sonido_bien = pygame.mixer.Sound(
    os.path.join('data', 'bien.wav'))
sonido_repe = pygame.mixer.Sound(
    os.path.join('data', 'repe.wav'))
sonido_gano = pygame.mixer.Sound(
    os.path.join('data', 'exito.ogg'))
sonido_fracaso = pygame.mixer.Sound(
    os.path.join('data', 'fracaso.ogg'))

#### poner texto
fuente = pygame.font.SysFont('courier', 48)



def mensaje_fin(screen, gana):
    fuente = pygame.font.SysFont('arial', 52)
    if gana:
        texto = u"Fin. Enhorabuena."
    else:
        texto = u"Fin. Otra vez será."    
    texto_fin = fuente.render(texto ,1 , (255, 0, 0))
    posicion_texto = texto_fin.get_rect()
    posicion_texto.centerx = screen.get_rect().centerx
    posicion_texto.centery = screen.get_rect().centery
    
    screen.blit(texto_fin, posicion_texto)
    
def dame_palabra():
    f = open(os.path.join('data', 'palabras.txt'))
    palabras = f.readlines()
    palabra = random.choice(palabras)
    f.close()
    return palabra.strip()



num = 0 ## repeticiones --> nombres de imágenes
palabra_oculta = dame_palabra()
errores = 0
introducidas = ""

def dame_letra(evento):
    letra = evento.unicode
    if letra.isalpha():
        return letra
    else:
        return None
    
def muestra_texto(oculta, introducidas):
    muestra = ""
    for letra in oculta:
        if letra in introducidas:
            muestra = muestra + letra+ ' '
        else:
            muestra = muestra + "_ "
    return muestra

### texto
texto_muestra = muestra_texto(palabra_oculta, introducidas)
texto = fuente.render(texto_muestra ,1 , (10, 10, 10))
posicion_texto = texto.get_rect()
posicion_texto.centerx = screen.get_rect().centerx
posicion_texto.centery = 280
                        
fondo = pygame.image.load(
                        os.path.join('data', '0.jpg'))
fondo = fondo.convert()
screen.blit(fondo, (0,0))
screen.blit(texto, posicion_texto)
pygame.display.flip()

fin = False

while True:
    events = pygame.event.get()
    for event in events:
        # Detección cierre ventana
        if event.type == QUIT:
            sys.exit(0)
        # Pusa una tecla?
        if event.type == KEYDOWN:
            # Si pulsa escape también salimos
            if event.key == K_ESCAPE:
                sys.exit(0)
            # Fin indica que ha ganado el jugador o que ha perdido (7 errores)
            if not fin:
                # Extrae la letra a partir del evento
                letra = dame_letra(event)
                # Es una letra? Ha podido teclear otro carácter
                if letra:
                #Había tecleado ya esa letra? No se cuenta como error
                    if letra in introducidas:
                        sonido_repe.play()
                    # Letra nueva: puede ser buena o mala: añadimos a introducidas y comprobamos
                    else:
                        introducidas = introducidas + letra
                        # letra mala: un error más, ha llegado a los 7?
                        if letra not in palabra_oculta:
                            errores = errores + 1
                            sonido_mal.play()
                            fondo = pygame.image.load(
                                os.path.join('data', '%d.jpg' % (errores)))
                            fondo = fondo.convert()
                            if errores == 7:
                                fin = True
                        # letra buena: componemos la nueva palabra a mostrar (se cambiarán
                        # uno o más guiones por la letra
                        # ha ganado ya?
                        else:
                            texto_muestra = muestra_texto(palabra_oculta, introducidas)
                            # ha ganado
                            if '_' not in texto_muestra:
                                sonido_gano.play()
                                fin = True
                            # todavía no ha ganado
                            else:
                                sonido_bien.play()
                        # Se recompone la pantalla: fondo, texto, mensaje de fin
                        screen.blit(fondo, (0,0)) 
                        texto = fuente.render(texto_muestra ,1 , (10, 10, 10))
                        screen.blit(texto, posicion_texto)
                        if fin:
                            if errores == 7:
                                mensaje_fin(screen, False)
                                sonido_fracaso.play()
                            else:
                                mensaje_fin(screen, True)
                                sonido_gano.play()
                        pygame.display.flip()


    #num = num + 1
    ##sonido.play()
    #pygame.time.delay(4000) # 1 segundo de retardo
