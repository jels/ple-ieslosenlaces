## Documentación ##
  * http://svnbook.red-bean.com/nightly/es/index.html
  * http://www.kopernix.com/?q=node/41
  * http://www.mononeurona.org/pages/display/746
  * http://prhlt.iti.es/seminars/2007/Andres07b.pdf

## Crear nuevo proyecto ##
```
$ mkdir NombreMiProyecto
$ cd NombreMiProyecto
$ mkdir branches tags trunk
# colocar ficheros en el trunk si ya tenemos
$ svn import . http://pepinon.inf.enlaces/plesvn/NombreMiProyecto -m "Inicio Proyecto" --username miuser
$ cd ..
$ rm -rf NombreMiProyecto
$ svn checkout http://pepinon.inf.enlaces/plesvn/NombreMiProyecto/trunk NombreMiProyecto
$ cd NombreMiProyecto
...
```

## Ignorar ficheros ##
```
$ nano /.subversion/config file.
[miscellany]
global-ignores = build *.pyc *.~ 
```

## Crear etiquetas / ramas ##
Esto crea una etiqueta (tag) "v0.1" de la versión **trunk** del momento.
```
$ svn copy http://pepinon.inf.enlaces/plesvn/NombreMiProyecto/trunk 
           http://pepinon.inf.enlaces/plesvn/NombreMiProyecto/tags/v.01
           -m "tag para versión 0.1"
```

## Analizar el proceso ##
```
$ svn log
```

## Crear ficheros de cambios ##
Ej. Cambios desde la revisión 42
```
$ cd ~/Proyectos/MiProyecto
$ svn log -r42:HEAD >> ChangeLog
$ svn commit ChangeLog -m 'Actualizar fichero de cambios'
```
Si tenemos instalado el paquete subversion-tools también podemos usar `svn2cl`. Esta utilidad está disponible también en http://ch.tudelft.nl/~arthur/svn2cl
```
$ svn2cl http://pepinon.inf.enlaces/plesvn/NombreMiProyecto/trunk -o ChangeLog
```

## Crear un archivo comprimido con una versión de nuestro programa ##
  1. Preparar copia
```
$ svn export  http://pepinon.inf.enlaces/plesvn/juego_naves_clase/tags/v.01 juego_naves_01
```
  1. Crear archivo comprimido
```
$ tar zcvf juego_naves_01.tgz juego_naves_01
```
  1. Eliminar copia temporal
```
$ rm -r juego_naves_01
```