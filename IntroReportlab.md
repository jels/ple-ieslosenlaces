

# Documentación #
## Oficial ##
  * http://www.reportlab.org/rl_toolkit.html
  * http://www.reportlab.com/docs/reportlab-userguide.pdf
  * Interesante colección de ejemplos: http://www.reportlab.org/contribs.html
## Artículos y blogs ##
  * http://www.linux-magazine.es/issue/13/ReportLab.pdf
  * http://maengora.blogspot.com/2008/12/leccin-no-8.html
  * http://www.devshed.com/c/a/Python/Python-for-PDF-Generation/
  * http://radicalpython.blogspot.com/2009/01/reportes-con-python-i-de-ii.html
# Instalación #
## con setuptools ##
```
$ easy_install reportlab
```
## Desde el fuente ##
  * Descargar último estable (http://www.reportlab.org/ftp/ReportLab_2_3.tar.gz)
  * Installar Python Imaging Library para usar imágenes png o gif (http://www.pythonware.com/products/pil/)
    * http://effbot.org/downloads/Imaging-1.1.6.tar.gz
> En ambos paquetes:
```
$ python setup.py build
$ sudo python setup.py install
```

## Problemas con Imaging ##
Editar setup.py (línea 41). Cambiar `TCL_ROOT = None` por `TCL_ROOT = "/usr/include/tk"`

# ¿Cómo se usa? #
Reportlab tiene tres formas (APIs) de uso:
  * [Canvas](ReportlabCanvas.md)
  * [Platypus](ReportlabPlatypus.md)
  * [Drawing](ReportlabDrawing.md)