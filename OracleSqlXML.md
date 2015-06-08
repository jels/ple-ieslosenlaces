
# Algo de doc #
## oracle ##
  * http://download.oracle.com/docs/cd/B28359_01/appdev.111/b28369/xdb13gen.htm
  * http://download.oracle.com/docs/cd/B28359_01/appdev.111/b28369/xdb11jav.htm#g1039140
  * https://oracle.sys-con.com/node/111252?page=0%2C0
  * http://www.zonaoracle.com/resources/oracle_xml.doc
  * http://www.filibeto.org/sun/lib/nonsun/oracle/10.2.0.1.0/B19306_01/appdev.102/b14259/xdb11jav.htm#g1039140
  * http://www.adp-gmbh.ch/ora/sql/xmlelement.html
  * https://oracle.sys-con.com/node/299947
  * http://gemsres.com/story/nov06/299947/source.html

# Intentos fallidos #
## con zxJDBC ##
```
from com.ziclix.python.sql import zxJDBC
d, u, p, v = "dbc:oracle:thin:@172.30.6.190:1521/enlaces5", 'dai1', 'tiger', "oracle.jdbc.driver.OracleDriver"


db = zxJDBC.connect(d, u, p, v)

cursor = db.cursor()
#[ ... ]
con3 = """Select
   c.CustId,
      xmlelement(name customer,
         xmlelement(name name, c.Name),
         xmlelement(name address, c.Address)) as CustInfo
from customer c"""

cursor.execute(con3)

for l in cursor.fetchall():
    print l
```

```
Traceback (most recent call last):
  File "conexion_zx.py", line 58, in <module>
    cursor.execute(con3)
zxJDBC.Error: error getting index [2], type [2.007] [SQLCode: 0]

```

## con cx\_oracle ##
```

import cx_Oracle

conexion='dai1/tiger@ENLACES5'
con3 = """select custid,name, address from customer"""

db_conn = cx_Oracle.connect(conexion)
cursor = db_conn.cursor()
cursor.execute(con2)
for l in cursor.fetchall():
    print l
```
```
(100, <cx_Oracle.OBJECT object at 0x8b5ad20>)
(101, <cx_Oracle.OBJECT object at 0x8b5ad40>)
(102, <cx_Oracle.OBJECT object at 0x8b5ad60>)
(103, <cx_Oracle.OBJECT object at 0x8b5ad80>)
(104, <cx_Oracle.OBJECT object at 0x8b5ada0>)
(105, <cx_Oracle.OBJECT object at 0x8b5adc0>)
(106, <cx_Oracle.OBJECT object at 0x8b5ade0>)
(107, <cx_Oracle.OBJECT object at 0x8b5ae00>)
(108, <cx_Oracle.OBJECT object at 0x8b5ae20>)
```