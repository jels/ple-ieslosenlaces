


# Java en Ubuntu #
  * http://www.guia-ubuntu.org/index.php?title=Java
  * InstalarEclipse
## Instalar java de Oracle ##
Documentación: http://sites.google.com/site/easylinuxtipsproject/java#TOC-INSTALL-MANUALLY
  * Descargar de http://www.oracle.com/technetwork/java/javase/downloads/index.html
  * Crear directorios y copiar:
```
$ sudo mkdir -p /opt/java/32
$ sudo cp jdk-6u23-linux-i586.bin /opt/java/32
```
  * Ejecutar:
```
sudo sh /opt/java/32/jdk-6u23-linux-i586.bin
sudo update-alternatives --install "/usr/bin/java" "java" "/opt/java/32/jdk1.6.0_23/bin/java" 1
```

# Documentación #
  * http://www.humbertocervantes.net/dokuwiki/doku.php?id=cursos:introjava:inicio
  * http://ocw.uc3m.es/informatica/programacion/transparencias
  * http://knuth.luther.edu/~bmiller/JavaForPython.html

  * http://math.hws.edu/javanotes/
  * http://javahispano.org/documentacion/

# Primeros pasos #
  * EjerciciosJava
  * Todo programa Java tiene que definir una clase. Todo el código está dentro de una clase.
  * Todo en Java tiene que tener un tipo predefinido.
  * Todo programa Java tiene que tener una función llamada `public static void main(String[] args)`.
  * Separación de bloques con llaves: `{`}
  * Indentación no obligatoria
  * final de sentencia: `;`
## Hola Mundo ##
```
public class HolaMundo {
    public static void main(String[] args) {
	System.out.println("Hola, Mundo");
	}
}
```
## Tipos de datos ##
## Numéricos ##
  * Tipos primitivos no son objetos en Java
  * Entrada y salida
## Import ##
Podemos usar cualquier clase con dos condiciones:
  1. javac y java saben que la clase existe (directorio actual o CLASSPATH)
  1. Nombre completo de la clase

Sistema jerárquico para acceder a las clases: paquete y clase.

El cargador se encarga de cargar las clases en memoria.
### CLASSPATH ###
  1. jar que contiene clases de java
  1. directorios con ficheros de clases
## Scanner ##
```
import java.util.Scanner;
.hasNext()
.hasNextInt()
.hasNextFloat()
.hasNextDouble()
.nextInt()
.nextFloat()
.next()
.useDelimiter("\n")
```

## Cadenas ##
`String cadena;`
Equivalencias python - java
```
str[3] 	        str.charAt(3) 	
str[2:5] 	str.substring(2,4)
len(str) 	str.length() 	
str.find('x') 	str.indexOf('x')
str.split() 	str.split('s') 
str.split(',') 	str.split(',') 
str + str 	str.concat(str)
str.strip() 	str.trim() 	
```

## Listas ##
JavaListas

## Diccionarios ##
JavaDiccionarios

## Condicionales ##
JavaCondicionales

## Excepciones ##
```
try {
   código de riesgo, que puede dar problemas: abrir archivo ...
}
catch (Exception e) {
   Si ocurre un error en el bloque try, se lanza la excepción
   Aquí se captura la excepción
}
```

## Bucles ##
JavaBucles

# Ficheros #
http://www.chuidiang.com/chuwiki/index.php?title=Lectura_y_Escritura_de_Ficheros_en_Java
# Swing #
> JavaSwing
# Ejercicios #
  * http://www.jtech.ua.es/plj/ejercicios.htm
  * http://math.hws.edu/javanotes/c6/exercises.html
  * http://www.humbertocervantes.net/dokuwiki/doku.php?id=cursos:introjava:practica1