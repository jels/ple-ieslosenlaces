# Bases de datos relacionales con python #

## dbapi ##
  * http://wiki.python.org/moin/DatabaseProgramming/
  * http://www.amk.ca/python/writing/DB-API.html
  * http://www.python.com.ar/moin/DbApi  (en español)
  * http://mundogeek.net/archivos/2008/06/25/bases-de-datos-en-python (en español)

## ejemplo con sqlite ##

Observa el ejemplo de http://mundogeek.net/archivos/2008/06/25/bases-de-datos-en-python/:
```
import sqlite3 as dbapi

# 1. Creamos objeto conexión
bbdd = dbapi.connect("bbdd.dat")

# 2. Creamos un cursor
cursor = bbdd.cursor()

# 3. Usamos cursor para acceder a la  base de datos
# 3.1. create
cursor.execute("""create table empleados (dni text,
                  nombre text,
                  departamento text)""")

# 3.2. insert
cursor.execute("""insert into empleados
                  values ('12345678-A', 'Manuel Gil', 'Contabilidad')""")

bbdd.commit()

# 3.3 select
cursor.execute("""select * from empleados
                  where departamento='Contabilidad'""")

# extraer resultados de select --> están almacenados en cursor
for tupla in cursor.fetchall():
    print tupla
```

## ejemplo con mysql ##
  * http://www.codegood.com/downloads
  * http://www.cbs.dtu.dk/biotools/mysql_tut/todo.html#_TOC041
```
import MySQLdb

dbusername = "user" 
dbname = 'user_private' 
dbpassword = 'some_password'

# connect to the database 
db = MySQLdb.Connect(db = dbname, user = dbusername, passwd = dbpassword)

#To perform a query, you first need a cursor, and then you can execute queries on it. 
cursor = db.cursor()

# create the query 
query = "SELECT * FROM foo"

# execute the query 
cursor.execute(query)

# retrieve the result 
results = cursor.fetchall()

for firstname, age, city in results: 
    print firstname, age, city 

```