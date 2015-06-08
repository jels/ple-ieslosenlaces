
# Instalar cliente de Oracle #
(Basado en http://marcelosoft.blogspot.com/2008/10/cmo-conectarse-oracle-desde-python-en.html)

## Descargar el Oracle InstantClient para nuestra plataforma Linux ##
http://www.oracle.com/technology/tech/oci/instantclient/index.html.
Paquetes necesarios:
  * Instant Client Package - Basic Lite
  * Instant Client Package - SDK
## Descomprimir y copiar ##
Primero hay que descomprimir los 2 archivos .zip; por ejemplo:
```
~$ unzip instantclient-basiclite-linux32-11.1.0.7.zip
~$ unzip instantclient-sdk-linux32-11.1.0.7.zip
```

Al descomprimir ambos archivos en el mismo directorio se generó el nuevo directorio **instantclient\_11\_1**.

Creamos el directorio `/opt/oracle`, y después lo movemos al nuevo directorio renombrado como `/opt/oracle/instantclient`
```
~$ sudo mkdir -p /opt/oracle/
~$ sudo mv instantclient_11_1 /opt/oracle/instantclient
```
## Configurar el linker ##
Configurar el linker para que encuentre las nuevas librerías instaladas. Importante ejecutar con `sudo -i` para obtener un shell inicial de root.
```
~$ sudo -i
[sudo] password for ****:
# echo "/opt/oracle/instantclient" > /etc/ld.so.conf.d/oracle.conf
# ldconfig
# ldconfig --print | grep /opt/oracle
# cd /opt/oracle/instantclient
# ln -s libclntsh.so.11.1 libclntsh.so
# ln -s libocci.so.11.1 libocci.so
```
  * Con `oracle.conf` introducimos un nuevo directorio no estándar de bibliotecas.
  * `ldconfig` refresca las bibliotecas disponibles.
  * Puedes comprobar la nueva ubicación con `# ldconfig --print | grep oracle`
  * Enlaces simbólicos al nombre (sin versión)
## ORACLE\_HOME ##
Luego, para poder compilar/construir primero e instalar después el módulo, hay que establecer la variable de entorno ORACLE\_HOME:
```
$ export ORACLE_HOME=/opt/oracle/instantclient/
```

# Instalación del cx\_Oracle #
## dependencias para instalar ... ##
(según el sistema en que estemos trabajando.
```
~$ sudo apt-get install python-dev python-setuptools build-essential
```

## Instalar desde el fuente ##
Descargar fuente de http://cx-oracle.sourceforge.net/ . Por ejemplo:
```
~$ tar xvzf cx_Oracle-5.0.tar.gz
~$ cd cx_Oracle-5.0/
~/cx_Oracle-5.0 $
```

```
~/cx_Oracle-5.0$ python setup.py build
```

Listo, ya podemos instalar y probar el nuevo módulo (con sudo si se instala para todos los ususarios):
```
~/cx_Oracle-5.0$ python setup.py install
```
## Instalar libaio1 ##
Descargamos una libreria que nos falta:
```
~$ sudo aptitude install libaio1
```

## TNSNAMES ##
` $ sudo mkdir -p /opt/oracle/instantclient/network/admin`
Creamos el archivo `/opt/oracle/instantclient/network/admin/tnsnames.ora` con el siguiente contenido:
```
ENLACES5 =
  (DESCRIPTION =
    (ADDRESS_LIST =
      (ADDRESS = (PROTOCOL = TCP)(HOST = "direccion_ip_servidor_oracle")(PORT = 1521))
    )
    (CONNECT_DATA =
      (SERVICE_NAME = enlaces5)
    )
  )
```
## Ejemplo de sesión ##
```
>>> import cx_Oracle
>>> conexion='usuario/contraseña@ENLACES5'
>>> db_conn = cx_Oracle.connect(conexion)
>>> cursor = db_conn.cursor()
>>> cursor.execute('SELECT ename FROM emp')
>>> registros = cursor.fetchall()
>>> for r in registros:
        print str(r)
('KING',)
('BLAKE',)
('CLARK',)
...
```
# Documentación #
  * http://wiki.python.org/moin/Oracle
  * http://marcelosoft.blogspot.com/2008/10/cmo-conectarse-oracle-desde-python-en.html
  * http://cx-oracle.sourceforge.net/
  * http://wiki.oracle.com/page/Installing+Oracle+&+Python+on+Linux