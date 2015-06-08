# Setup Tools #

Para instalar las setup tools que nos permitirán usar easy\_install, vamos a http://peak.telecommunity.com/dist/ez_setup.py copiamos el contenido en el idle de python por ejemplo y lo guardamos como ez\_setup.py en la carpeta de Python26 que esta instalado por defecto en C:\Python26

Una vez guardado lo arrancamos como un programa normal, y nos descargará easy\_install

# Instalar pycha y reportlab mediante easy\_install #

Si quereis podemos meter easy\_install en el path de windows para no tener que ir a la carpeta donde tenemos easy\_install de la siguiente manera:

Botón derecho sobre MiPc -> Propiedades -> Opciones avanzadas -> Variables de Entorno
En la ventanita de Variables del sistema buscamos "Path" y hacemos doble click y sin borrar nada en la casilla de valor de variable nos colocamos al final y escribimos ";C:\Python26\Scripts" (El punto y coma es para marcar que empieza un valor nuevo y que no lo mezcle con el anterior, y la dirección es el directorio por defecto en el que tendremos el easy\_install)

En caso de que no lo metamos en el path, simplemente nos colocamos en el directorio del easy\_install C:\Python26\Scripts(por defecto) y escribimos:
```
easy_install pycha
```
Asi nos instalará pycha, una vez haya terminado escribimos:
```
easy_install reportlab
```

# Instalar pycairo #

Descargamos pycairo para la version 2.6 de python de http://ftp.gnome.org/pub/GNOME/binaries/win32/pycairo/1.4/

Lo instalamos, ahora necesitamos unas librerias que descargaremos de http://www.gtk.org/download-windows.html bajamos hasta llegar a la seccion "GTK+ individual packages"
y de ahí descargamos cairo dandole a binaries, zlib y libpng.

Una vez descargadas copiamos las respectivas .dll en la carpeta de cairo que se encuentra por defecto en "C:\Python26\Lib\site-packages\cairo"