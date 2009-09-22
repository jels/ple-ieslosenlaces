import random
import time

class Heroe(object):
    """
    Descripción de la clase
    """
    def __init__(self, nombre, num_vidas=10):
        self.nombre = nombre
        self.poder = num_vidas
    def ataca(self, enemigo):
        if self.poder > 0:
            print "Espanto a enemigo"   
            self.poder = self.poder - 1
            enemigo.huir()
        else:
            print "No tengo power ...  :-("
    def estoy_vivo(self):
        if self.poder > 0:
            return True
        else:
            return False

class Alien(object):
    def __init__(self, vidas):
        self.vidas = vidas
    def huir(self):
        self.vidas = self.vidas - 1
        print "Me voy porque me atacan ... (%d vida)" % (self.vidas)
    def estoy_vivo(self):
        if self.vidas > 0:
            return True
        else:
            return False

jefe = Heroe('Superman')
a1 = Alien(4)
a2 = Alien(3)
a3 = Alien(2)

lista_aliens = [a1, a2, a3]

def limpia_lista(aliens):
    for alien in aliens:
        if not alien.estoy_vivo():
            aliens.remove(alien)

            
            

while jefe.estoy_vivo():
    if len(lista_aliens) == 0:
        break
    jefe.ataca(random.choice(lista_aliens))
    limpia_lista(lista_aliens)
    time.sleep(0.5)
    
if len(lista_aliens) > 0:
    print "Pierde jugador, quedan %d aliens" % len(lista_aliens)
else:
    print "Gana jugador"

    
    


