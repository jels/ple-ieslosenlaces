

# Ubuntu #
## Versión que viene con el sistema ##
```
$ sudo aptitude install eclipse-pydev 
```

# Windows #
  * Descargar JSE http://java.sun.com/javase/downloads/index.jsp
  * Descargar eclipse: http://www.eclipse.org/downloads/

# Desde la web #
  * http://www.eclipse.org/downloads/  --> Eclipse IDE for Java Developers (85 MB)
  * Si se quiere poner en español, añade el sitio de i18n a los sites de update: http://download.eclipse.org/technology/babel/update-site/R0.8.0/helios


# Pydev #
Ha cambiado el proyecto. Ahora se ha integrado en aptana. Página inicial de pydev: http://pydev.org/
Se instala desde eclipse como todo:
```
Ayuda --> Instalar nuevo software --> Add / Añadir --> http://pydev.org/updates
```
Documentación:
  * http://pydev.org/manual.html
  * http://tomatesasesinos.com/tutoriales/pythonEnEclipse.html

# Instalar subclipse #
(para usar subversion)
  * http://subclipse.tigris.org/install.html
  * http://www.migue.org/diario/2007/08/cmo-usar-subversion-en-eclipse.html

# Instalar EclipseMercurial #
(para usar mercurial)
  * sitio: http://javaforge.com/project/HGE
  * site para añadir: http://cbes.javaforge.com/update



# Chuleta de Pablo #

## Instalar Ecplipse: ##

  * Descargar la version eclipse que quieras de la pagina web http://www.eclipse.org/downloads/ (version de 85mb)

  * Descargar babel http://www.eclipse.org/babel/downloads.php

  * Descomprimimos las dos carpetas en el escritorio (por ejemplo), primero eclipse y luego babel

Ya tenemos eclipse en su ultima version y en castellano



## Desarrollar en Python utilizando eclipse ##
  * Abrimos eclipse > ayuda > software updates > encontrar e instalar

Tenemos que instalar Pydev, para ello sabemos que necesitamos (http://pydev.sourceforge.net/download.html)

  * olvemos a exlipse y le damos a la pestaña Add site, para nuestra version actual utilizamos esta direccion http://pydev.sourceforge.net/updates/

Tambien queremos añadir a eclipse el modulo necesario para poder usar subversion, esta es subclipse http://subclipse.tigris.org/install.html
  * eguimos el procedimiento anterior para añadirle el modulo http://subclipse.tigris.org/update_1.4.x

  * ceptamos las licencias y le damos Finish


Si queremos desarrollar en otro lenguaje que no sea java, vamos a perspectivas, otras perspectivas y alli tenemos que encontrar todos los modulos instalados en el sistema.
Seleccionamos pydev y aceptamos.
Carga una serie de modulos y crea la perspectuva Pydev

Si el python de systema es python 2.5 y queremos usar 2.6
Vamos a
**ventana > preferencias > Pydev > Editor > interpreter - Python**
Le damos a nuevo y seleccionamos la ruta de nuestro python 2.6 /usuario/lib/python2.6/python
Una vez añadido lo subimos para que por defecto utilice siempre el 2.6


Para empezar a trabajar
**Archivo > Nuevo > proyecto de pydev**
Por defecto todo se guarda en el workspace configurado al inicio
Si queremos cambiar la ubicacion desactivamos el use default y le decimos la ruta
Damos nombre al archivo
Podemos elegir el proyecto entre Python o Jython la version de sintaxis y el interprete
Desactivamos la carpeta para crear src
Si hace referencia a otro proyecto podemos en la ventana siguiente decirle a que proyecto esta vinculado