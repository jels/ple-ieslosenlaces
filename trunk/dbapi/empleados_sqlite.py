# -*- coding: utf-8 -*-
# importar módulo
import sqlite3 as dbapi
from pprint import pprint

# conexión
con = dbapi.connect('ejemplo.bd')

"""
>>> dbapi.apilevel
'2.0'
>>> dbapi.paramstyle
'qmark'
>>> dbapi.sqlite_version
'3.5.9'
>>> dbapi.threadsafety
1
>>> dbapi.version
'2.4.1'
"""
# creación cursor
cursor = con.cursor()
# create table
sentencia_creacion = """create table empleados (dni text,
nombre text, departamento text)"""
#cursor.execute(sentencia_creacion)
# insert
sentencia_insertar = "insert into empleados values (?, ?, ?)"
#cursor.execute(sentencia_insertar, ('123456', 'Damir', 'DAI'))
empleados = (('2222222', 'Pablo', 'DAI'),
             ('3333333', u'Jesús', 'DAI'),
             ('444444', 'Alejandra', 'DAI'),
             ('555555', 'Carmen', u'Dirección')
             )
cursor.executemany(sentencia_insertar, empleados)
# select
cursor.execute('select * from empleados')
for em in cursor.fetchall():
    print "%-12s %-10s %-10s" % em 
