# Ejercicios Java #
  1. Pedimos los lados de un cuadrado y mostramos su área.
  1. Pedimos radio del círculo y mostramos área y circunferencia.
  1. Pedimos 10 números y mostramos la media.
  1. Pedimos 10 números y mostramos el mayor, el menor y la media.
  1. Pedimos 5 nombres de personas y su edad, mostramos el nombre de la de mayor edad.
  1. Números primos menores 100
    1. Var1. El número lo pedimos al usuario
    1. Método `static boolean esPrimo(int i) `
  1. Escribe un programa que pida una serie de números. El programa termina cuando no se introduce ningún número (entrada en blanco). El programa mostrará la lista de números introducidos, el menor, el mayor y la media.
  1. Crea una clase Persona (`Persona.java`). Almacenaremos el nombre, la edad y el número de hijos de esa persona. Añadiremos un método `.cadena()` que devuelva una cadena con su nombre y edad.
    1. Crea  una nueva clase `PruebaPersona` con un método `static void main(String[] args)` para hacer una prueba de que funciona bien.
    1. Los campos nombre, número de hijos y edad serán privados.
    1. Crea métodos públicos (setNombre) que tome como parámetro el nuevo nombre.
    1. Crea métodos públicos (getNombre) que devuelva el nombre.
    1. Modifica el `main`.
    1. Crea dos constructores. Uno con parámetros y otro sin parámetros. El que no tiene parámetros pondrá como nombre anónimo.
    1. Añade una variable estática para almacenar el número total de personas que se creen. Modifica los constructores.
    1. Crea un método estático que muestre los elementos de un vector de personas. Haz un programa que cree un vector de 5 personas y los muestre en pantalla.
    1. Crea un método de clase que tome como parámetros un nombre y un vector de personas y devuelva la posiciópn de esa persona dentro del vector o -1 si no está en el vector.
  1. Crea una clase Fecha con los siguientes métodos:
    1. `Fecha(int dia, int mes, int anio)`
    1. `Fecha()`  --> fecha del día
    1. `boolean anterior(Fecha f)`  --> devuelve verdadero si la fecha es anterior a f.
    1. `boolean equal(Fecha f)`
    1. `int dia()`
    1. `int mes()`
    1. `int anio()`
    1. `int diaSemana()` --> día de la semana: 1=lunes, 2=martes ...
    1. `String toString()`
  1. Añade a Persona un atributo para almacenar la fecha de nacimiento.
  1. Crea una clase `Empleado` que guarde los datos de nombre, número de hijos, fecha de nacimiento y categoría (un núm. entero). La clase Empleado derivará de Persona.
    1. Define los métodos necesarios.
    1. Añade método `.toString()`
  1. Haz que la clase persona implemente el interfaz `Comparable` ordenando según el nombre de la persona. ==> crea el método `compareTo(Persona p`
    1. Utiliza un vector de personas (ArrayList) para comprobarlo.






