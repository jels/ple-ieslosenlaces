## Instalar un driver ##
Lo hemos documentado en InstalarCxOracleEnUbuntu
  * http://wiki.python.org/moin/Oracle
  * http://marcelosoft.blogspot.com/2008/10/cmo-conectarse-oracle-desde-python-en.html
  * http://cx-oracle.sourceforge.net/
  * http://wiki.oracle.com/page/Installing+Oracle+&+Python+on+Linux

## Conexión ##
```
dsn = cx_Oracle.makedsn('host.com', int(1534), 'dbname')
my_db = cx_Oracle.connect('username', 'password', dsn )
cursor = my_db.cursor()
cursor.execute("SELECT a, b, c FROM sometable")
rows = cursor.fetchall()
```

## Ejemplo de uso ##
Ejecutamos python:
```
$ ipython
In [1]: import cx_Oracle

In [2]: conexion='usuario/contraseña@direccion_ip_servidor_oracle:1521/cadena_conexion'

In [3]: db_conn = cx_Oracle.connect(conexion)

In [4]: cursor = db_conn.cursor()

In [5]: cursor.execute('SELECT ename FROM emp')

In [6]: registros = cursor.fetchall()

In [7]: for r in registros:
...:        print str(r)
...:
...:
('KING',)
('BLAKE',)
('CLARK',)
('JONES',)
('MARTIN',)
('ALLEN',)
('TURNER',)
('JAMES',)
('WARD',)
('FORD',)
('SMITH',)
('SCOTT',)
('ADAMS',)
('MILLER',)
```