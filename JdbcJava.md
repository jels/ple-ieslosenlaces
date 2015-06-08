
# Intro #
  * http://java.sun.com/docs/books/tutorial/jdbc/basics/
  * http://www.itapizaco.edu.mx/paginas/JavaTut/froufe/parte21/cap21-4.html
  * http://www.proactiva-calidad.com/java/jdbc/index.html


# Instalación de JDBCs #
(Propuesta de Chema en http://listas.aditel.org/archivos/python-es/2006-June/013052.html)

_Los ficheros jars deben estar en el CLASSPATH. Lo que yo hago es crearme
mi propio script para ejecutar jython:_

```
#!/bin/bash

JDBCPATH=/opt/jdbc-drivers

CLASSPATH=$CLASSPATH:$JDBCPATH/mysql.jar
CLASSPATH=$CLASSPATH:$JDBCPATH/oracle.jar
CLASSPATH=$CLASSPATH:$JDBCPATH/informix.jar
CLASSPATH=$CLASSPATH:$JDBCPATH/postgresql.jar
CLASSPATH=$CLASSPATH:$JDBCPATH/mssql.jar
export CLASSPATH

/usr/local/bin/jython "$@"
```

# Clases #
![http://www.itapizaco.edu.mx/paginas/JavaTut/froufe/parte21/cap21-11.gif](http://www.itapizaco.edu.mx/paginas/JavaTut/froufe/parte21/cap21-11.gif)