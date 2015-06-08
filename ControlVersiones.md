

# Documentación general #
  * http://es.wikipedia.org/wiki/Control_de_versiones

# Mercurial #
## Documentación fácil ##
  * http://www.adictosaltrabajo.com/tutoriales/tutoriales.php?pagina=mercurial
  * http://www.losersjuegos.com.ar/incoming/descargas/20101217/pilas_desarrolladores.pdf
  * https://developer.mozilla.org/es/FAQ_de_Mercurial

## Más docs ##
  * http://devnull.li/libromercurial/index.es.html
  * http://hginit.com/
  * http://www.joelonsoftware.com/items/2010/03/17.html
## Mercurial y eclipse ##
  * Mercurial y eclipse: http://www.vogella.de/articles/Mercurial/article.html
  * Mercurial, bitbucket y Netbeans: http://es.debugmodeon.com/articulo/control-de-versiones-con-netbeans-mercurial-y-bitbucket
  * Googlecode, eclise y mercurial: http://blogs.intland.com/main/entry/39

# GIT #
  * http://library.edgecase.com/git_immersion/index.html

# Subversion #
## Intro ##
  * http://es.wikipedia.org/wiki/Subversion
  * http://svnbook.red-bean.com/nightly/es/index.html
  * http://macprogramadores.org/tutoriales/tutoriales/cvssvn.pdf
  * http://picandocodigo.net/downloads/docs/subversion-presentacion-01.pdf
  * http://picandocodigo.net/downloads/docs/subversion-presentacion-02.pdf
## Referencia rápida ##
  * http://polaris.dit.upm.es/~rubentb/docs/subversion/TutorialSubversion/ar01s03.html
  * http://www.addedbytes.com/cheat-sheets/subversion-cheat-sheet
## Instalación ##
  * Instalación de subversion en ubuntu: http://www.fileden.com/files/2007/6/10/1162529/Manual%20Subversion%20Ubuntu.pdf
## Ciclo de trabajo ##
**Crear copia local**
```
$ svn checkout 
```
**Actualizar copia local**
```
$ svn update
```
**Hacer cambios**
```
$ svn add
$ svn delete
$ svn copy
$ svn move
```
**Examinar cambios**
```
svn status
svn diff
```
**Deshacer algunos cambios**
```
$ svn revert
```
**Resolver conflictos (merge con los cambios de otros)**
```
$ svn update
$ svn resolve
```
**Convirmar tus cambios**
```
$ svn commit ­m ”Mensaje”
```