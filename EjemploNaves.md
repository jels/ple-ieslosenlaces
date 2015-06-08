Ejemplo de: http://floppsie.comp.glam.ac.uk/Glamorgan/gaius/games/10.html

## Tarea ##
Hay que optimizar el ejemplo.
  * Podemos evitar el uso de tantas variables globales, usando atributos de clase
  * Podemos usar grupos de sprites: http://miprogramacionenjuegos.wordpress.com/2007/05/15/la-clase-sprite/

```
#!/usr/bin/python
# -*- encoding: utf-8 -*-


import pygame
import sys
from pygame.locals import KEYDOWN, KEYUP, K_SPACE, K_ESCAPE, \
                          K_RIGHT, K_LEFT

width         = 320
height        = 240
imageWidth    = 32
imageHeight   = 32


goingLeft     = True
invaderHeight = 0
gunLeft       = False
gunRight      = False
gunXpos       = (width/2)-(imageWidth/2)
delay         = 10


class BoxSprite(pygame.sprite.Sprite):
    image = None

    def __init__(self, initial_position):
        pygame.sprite.Sprite.__init__(self)
        if BoxSprite.image is None:
            BoxSprite.image = pygame.image.load("ball.png")
        self.image = BoxSprite.image


        self.rect = self.image.get_rect()
        self.rect.topleft = initial_position
        self.next_update_time = 0  # as soon as possible
        self.yPos = initial_position[1]


    def update(self, current_time, left, right):
        global goingLeft, invaderHeight, imageWidth, delay
        # check update
        if self.next_update_time < current_time:
            # If we’re at the left or right the screen, switch directions.
            if self.rect.topleft[0] == left:
                goingLeft = False
                invaderHeight += 1
            elif self.rect.topleft[0] == right-imageWidth:
                goingLeft = True
                invaderHeight += 1
            if goingLeft == True:
                self.rect.topleft = [self.rect.topleft[0]-1, \
                                     self.rect.topleft[1]]
            else:
                self.rect.topleft = [self.rect.topleft[0]+1, \
                                     self.rect.topleft[1]]
            self.rect.topleft = [self.rect.topleft[0], \
                                 invaderHeight+self.yPos]
            self.next_update_time = current_time + delay


class missile(pygame.sprite.Sprite):
    image = None

    def __init__(self, initial_position):
        pygame.sprite.Sprite.__init__(self)
        if missile.image is None:
            missile.image = pygame.image.load("arrow.png")
        self.image = missile.image


        self.rect = self.image.get_rect()
        self.rect.topleft = initial_position
        self.next_update_time = 0 # update() hasn’t been called yet.


    def update(self, current_time, left, right):
        global missile
        # check update
        if self.next_update_time < current_time:
            # If we’re reached the top then stop
            if self.rect.topleft[1] == 0:
                missiles.remove(self)
                self.kill()
                return
            else:
                self.rect.topleft = [self.rect.topleft[0], \
                                     self.rect.topleft[1]-1]
            self.next_update_time = current_time + 4



class gun(pygame.sprite.Sprite):
    image   = None

    def __init__(self):
        global width, imageHeight, gunXpos
        pygame.sprite.Sprite.__init__(self)
        if gun.image is None:
            gun.image = pygame.image.load("gun.png")
        self.image = gun.image


        self.rect = self.image.get_rect()
        self.rect.topleft = [gunXpos, height-imageHeight]
        self.next_update_time = 0 # update() hasn’t been called yet.


    def update(self, current_time, left, right):
        global gunXpos, width, imageWidth


        # check update
        if self.next_update_time < current_time:
            if gunLeft and gunXpos>0:
                gunXpos -= 1
            if gunRight and gunXpos<width-imageWidth:
                gunXpos += 1
            self.rect.topleft = [gunXpos, self.rect.topleft[1]]
            self.next_update_time = current_time + 1


def checkInput():
    global gunLeft, gunRight, missiles, gunXpos, height
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit(0)
            elif event.key == K_RIGHT:
                gunLeft = False
                gunRight = True
            elif event.key == K_LEFT:
                gunLeft = True
                gunRight = False
            else:
                missiles.append(missile([gunXpos, height]))
        elif event.type == KEYUP and event.key != K_SPACE:
            gunRight = False
            gunLeft = False


def checkCollisions():
    global missiles, boxes
    if missiles != [] and boxes != []:
        for m in missiles:
            found = False
            for b in pygame.sprite.spritecollide(m, boxes, 0):
                boxes.remove(b)
                b.kill()
                found = True
        if found:
            missiles.remove(m)
            m.kill()



pygame.init()
boxes = []
missiles = []

for x in range(0, width, 32):
    for y in range(0, 96, 32):
        boxes.append(BoxSprite([x, y]))


screen = pygame.display.set_mode([320, 240])
gunControl = gun()


while boxes != []:
    screen.fill([0, 0, 0]) # blank the screen.
    time = pygame.time.get_ticks()
    for b in boxes:
        b.update(time, 0, width)
        screen.blit(b.image, b.rect)

    checkInput()
    checkCollisions()


    gunControl.update(time, 0, width)
    screen.blit(gunControl.image, gunControl.rect)
    for m in missiles:
        m.update(time, 0, width)
        screen.blit(m.image, m.rect)
    pygame.display.update()
    if pygame.sprite.spritecollide(gunControl, boxes, 0) != []:
        pygame.time.delay(50)
        print "looser"
        sys.exit(0)
    if len(boxes)<10:
        delay = len(boxes)
    pygame.time.delay(50)
print "winner"
```