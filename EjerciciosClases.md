# Ejercicios con clases #
## Modificar ejercicio dados ##
  1. Escribe una nueva clase Botón que cree botones circulares. Lama a tu nueva clase CBoton e implementa los mismos métodos que tiene la clase original Boton. El constructor tomará el centro delbotón y su radio como parámetros. Pon la clase en un nuevo módulo llamado cboton.py. Comprueba la nueva clase modificando el ejercicio de los dados.
  1. Modifica la clase Dado añadiendo un método que permita cmabiar el color de los puntos al especificado. (`.set_color(self, color` Cambia el color

## Figuras ##
  1. Escribe una clase que represente una esfera. La clase tiene que implementar los métodos siguientes:
    1. init(self, radio)  Crea una esfera con el radio indicado
    1. get\_radio(self)  Devuelve el radio de la esfera
    1. area(self) Devuelve el area de la superficie de la esfera
    1. volumen(self) Devuelve el volumen de la esfera.
  1. Escribe una clase que represente un cubo. El constructor tomará como parámetro el tamaño del lado de una cara.
  1. Crea una lista con cubos y esferas. Los radios y lados serán aleatorios. Escribe una función que tome como parámetro la lista y muestre enla pantalla:
    1. cúantas figuras de cada tipo hay
    1. volumen de las esferas y de los cubos
    1. volumen total de todas las figuras

## Cartas ##
(puede ayudarte este ejemplo: http://almacen.gulic.org/httlaclwp/chap15.htm)

  1. Implementa una clase que  represente una baraja. La clase tiene que tener los siguientes métodos:
    1. init(self, num\_carta, palo)
    1. get\_num(self)
    1. get\_palo(self)
    1. str(self) Devuelve una cadena con los nombres de las cartas: "As de oros" o "Sota de espadas".