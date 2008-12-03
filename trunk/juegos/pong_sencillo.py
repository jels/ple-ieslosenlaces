# -*- coding: utf-8 -*-


"""
Pong sencillo
Basado en http://www.purplestatic.com/gs/pdf/PONG.pdf
"""

import pygame
from pygame.locals import *
import sys

def main():
     # inicia pygame
     pygame.init()
     # crea una superficie (surface) para dibujar cosas dentro. Tamaño: 640 x 480 pixels
     screen = pygame.display.set_mode((640,480))
     # pone título en la pantalla
     pygame.display.set_caption("P O N G")
     # crea un espacio vacío para rellenar la pantalla
     background = pygame.Surface(screen.get_size())
     # convert --> agilizará el refresco después
     background = background.convert()
     # relleno con color negro
     background.fill((0,0,0))
     # dibuja el fondo de la pantalla
     screen.blit(background,(0,0))
     # crea la pelota: un rectángulo
     pelota = pygame.Rect( (320,240), (10,10))
     # crea la raqueta
     raqueta = pygame.Rect( (320,420), (70,10))
     # crea un objeto para mostrar los puntos / vidas
     punto = pygame.Rect( (10,10), (10,10))
     # inicia las variables
     pelotaVel = [1,1]
     velocidad = 1
     puntuacion = 3
     # bucle principal del juego
     while True:
          pygame.time.delay(5)
          # pinto el fondo
          screen.blit(background,(0,0))
          # muevo la pelota pelota
          pelota.left += pelotaVel[0] * velocidad
          pelota.top += pelotaVel[1] * velocidad
          # comprueba si se sale de la pantalla
          if pelota.center[0] > 635 or pelota.center[0] < 5:
               pelotaVel[0] *= -1
          if pelota.center[1] > 475 or pelota.center[1] < 5:
               pelotaVel[1] *= -1
          # comprueba si la pelota toca la raqueta
          if pelota.center[1] == 415:
               if pelota.center[0] > raqueta.left and pelota.center[0] < raqueta.right:
                    pelotaVel[1] *= -1
                    velocidad += 1
                    puntuacion += 1
                    print puntuacion
               else:
                    if pelotaVel[1] < 0:
                         puntuacion -= 1
                         print puntuacion
          # comprueba si se han pulsado las flechas y actualiza la raqueta.
          pulsadas = pygame.key.get_pressed()          

          if pulsadas[K_RIGHT]:
               raqueta.left += 5
          if pulsadas[K_LEFT]:
               raqueta.left -= 5
          # muestra la puntuación
          for i in range(puntuacion):
               punto.left = i * 20 + 10
               pygame.draw.rect(screen,(255,255,255),punto)
          # dibuja la pelota y la raqueta: rectángulos blancos
          pygame.draw.circle(screen,(255,255,255),pelota.center, 8)
          pygame.draw.rect(screen,(255,255,255),raqueta)
          
          # refresca la pantalla con los cambios hechos          
          pygame.display.flip()
          
          # han cerrado la ventana?
          for event in pygame.event.get():
                         if event.type == QUIT:
                              return
          if puntuacion == 0:
               return

# el programa llama a la función main/principal ..
if __name__ == "__main__": 
     main()
