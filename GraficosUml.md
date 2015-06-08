## autodia ##
### Descargar autodia ###
  * http://www.aarontrevena.co.uk/opensource/autodia/
  * http://cpan.dei.uc.pt/authors/id/T/TE/TEEJAY/Autodia-2.08.tar.gz
### Instalar ###
Descomprimir ...
```
$ perl Makefile.PL
$ make
$ make test
$ sudo make install
```
Instalar dependencias si hay errores ...
```
$ sudo aptitude install perl libtemplate-perl libgraphviz-perl
```
### Crear gráfico ###
```
$ autodia.pl -i <nombre_archivo.py> -l python -o <archivo_salida.dia>
```