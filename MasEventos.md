# Gestión de eventos con Pygame #
Basado en http://lorenzod8n.wordpress.com/2007/12/09/pygame-tutorial-4-more-on-events/

## Problemas con poll ##

Hemos usado `pygame.event.poll()` para recibir la información de los eventos. Pero hay más alternativas. El programa teiene un consumo muy elevado de CPU. Compruébalo (Gestor de tareas en windows o top en linux.

Haz esta prueba:
```
#! /usr/bin/env python
import pygame

screen = pygame.display.set_mode((640, 400))
running = 1
 
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    else:
        print event.type
```
Ejecuta el programa y estudia la salida. (Aviso: según el hardware, puede ralentizar mucho tu ordenador) Como puedes ver, el programa envía cantidades de ceros al terminal. Si colocas el ratón en la ventana y lo mueves un poco, verás que aparecen rápidamente otros números, pero casi siempre verás ceros.

Esto es porque el método poll() devuelve un evento de tipo NOEVENT si no hay ningún evento enla cola de eventos. Esto es muy derrochador. Necesitamos una forma mejor de escribir nuestro bucle de eventos. Usaremos `pygame.event.get()`. Debajo está el código modificado:
```
#! /usr/bin/env python
import pygame

screen = pygame.display.set_mode((640, 480))
running = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
        else:
            print event.type
```
Ahora tenemos un pequeño bucle `for` en lugar de llamar a `poll()` Este bucle recorre los eventos activos en la cola. Ejecuta el programa y compara la salida. ¡¡¡No hay ceros!!!  Esto es porque `pygame.event.get()` no genera **NOEVENTs**. Sólo se ven números cuando se mueve o hace clic con el ratón.

That takes care of part of the problem. However, if you go back to studying your CPU usage you will see that it is probably still high. It may be slightly lower, however. But we can still clearly do something about our CPU usage.

What is happening is that our program is so busy running through the event loop that it puts a lot of demand on the CPU. Imagine if we could get the program to take a pause once in a while, so that the CPU gets a chance to breathe out (and the operating system a chance to deal with other issues). That is exactly what we are going to do with a pygame.time.Clock().

For the time being it may be helpful to understand this as that we have a clock that we use to regularly tell our pygame program to “take a rest”. It will then signal to the rest of the system that, “hey, I’m idle at the moment, so do whatever it is you have to do”.

Creating the Clock() is only the first part, we also need to let it work. This is done inside the event loop. Simply call the tick() method on the Clock object. You can optionally pass in a number that I won’t go into too much because it will spoil one of the exercises. ;-)

The final version of our program then looks as follows:
```
#! /usr/bin/env python
import pygame

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = 1
while running:
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
   clock.tick(20)
```

Ntice that I have used clock.tick(20). In this case there is nothing happening on the screen, so the value I place there is rather irrelevant. But when you add “things” to your screen you will notice that the value you use will make a difference. Without going into too much detail, there is a trade-off between getting your program to run as fast as possible, and your resource usage spiking to the point where the computer becomes very slow.

What I have taught you here obviously means that you have to “unlearn” some of the things I taught you from the beginning. Sorry about that. But then again, it won’t be the last time.

I personally don’t like tutorials that say “do like this, don’t do like that”. I prefer to see things for myself. I hope that I have managed to get you to understand why you should write your programs in a certain way. My long-term goal is not just to let you be able to put together pygame programs, but to know exactly what you are doing as well.

That’s it for now. But this time you won’t have to wait as long for the next tutorial, I promise.

## Ejercicios ##

Rewrite every single application you have written so far as a part of the tutorial series, both the examples I have given as well as the exercise you have solved (because you have been doing the exercises, haven’t you?). In each case, re-write it to use pygame.event.get() instead of pygame.event.poll(). Also include a Clock().

For each program, compare CPU usage and responsiveness between the original version and your new version. Also, experiment with different values in the clock.tick() method call. Try a really large number. Then try a really small number. In each case, look at CPU usage. See how fast or slow the program runs. Based on what you see, what can you say about x in clock.tick(x)? How does a low or a high value of x affect responsiveness and speed of the application as well as CPU usage? Finally try to find a value that keeps your pygame application running as smoothly as possible but without making the rest of your computer too slow.