

## Solución muy sencilla con cx\_freeze ##
  1. Instalar cx\_freeze: http://cx-freeze.sourceforge.net/
  1. Ejecutar desde la consola:
```
c:\Python26\Scripts\cxfreeze <nombre_juego>.py --target-dir <directorio_destino> -OO -c  --icon=<icono.ico> --target-name=<nombre_exe>  --base=Win32GUI 
```
  1. copiar el directorio de datos en el dir destino del ejecutable.

## py2exe ##
  * http://www.py2exe.org
  * Descargar: http://sourceforge.net/projects/py2exe/files/
  * Tutorial: http://py2exe.org/index.cgi/Tutorial
  * http://www.blog.pythonlibrary.org/2010/07/31/a-py2exe-tutorial-build-a-binary-series/
  * En general (distribuir python): http://mundogeek.net/archivos/2008/09/23/distribuir-aplicaciones-python


### Resolver algunos problemas ###
  * http://crazedmonkey.com/blog/python/pkg_resources-with-py2exe.html

### Con wxpython ###
  * Documentación del wiki de wxpython: http://wiki.wxpython.org/index.cgi/DistributingYourApplication

### Con pygame ###
  * http://www.pygame.org/wiki/Pygame2exe
  * http://www.pygame.org/project/589/
  * Un ejemplo: http://code.google.com/p/pybreakout/source/browse/trunk/src/pybreakout/setup.py
### Con Qt ###
  * http://popdevelop.com/2010/04/how-to-build-an-executable-application-from-your-python-script-qt-special/
  * http://www.py2exe.org/index.cgi/Py2exeAndPyQt
  * http://arstechnica.com/open-source/guides/2009/03/how-to-deploying-pyqt-applications-on-windows-and-mac-os-x.ars/



## GUI2EXE ##
  * Proyecto interesante: http://code.google.com/p/gui2exe/

## py2app ##
  * http://aralbalkan.com/1675

## Wrappers ##
_py2exe me está dando problemas con las fuentes_
  * http://www.pygame.org/project-PySetup-589-.html
  * http://www.moviepartners.com/blog/utilities/ppb/

## nsis ##
  * http://nsis.sourceforge.net
  * http://foro.portalhacker.net/index.php/topic,76300.0.html

## innosetup ##
  * http://www.scribd.com/doc/27229302/Tutorial-de-Inno-Setup