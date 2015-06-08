# Apuntes pygame #

## listar modos de vídeo: ##

```
import pygame
pygame.init()
pygame.display.list_modes()
```
## flags del display: ##
```
import pygame
from pygame.locals import *

SCREEN_SIZE = (640, 480)
pygame.init()
screen = pybame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
# screen = pybame.display.set_mode(SCREEN_SIZE, FULLSCREEN, 32)
```

## font ##
  * lista de fuentes instaladas
```
pygame.font.get_fonts()
```
  * uso
```
fuente = pygame.font.SysFont("arial", 16)
text_surface = fuente.render("Pygame es cool!!", True, (0,0,0), (255, 255, 255))
# parámetros: texto, antialiased, color, fondo
```
  * prueba
```
import pygame
pygame.init()

mi_nombre = "Luis Miguel"
fuente = pygame.font.SysFont("arial", 64)
nombre_surface = fuente.render(mi_nombre, True, (0,0,0), (255,255,255))
pygame.image.save(nombre_surface, 'nombre.png')
```