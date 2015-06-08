
# Requisitos #
  * Instalar el conector de mysql para java: http://dev.mysql.com/downloads/connector/j/
  * Configurar entorno (CLASSPATH o librerías de eclipse)

# Ejemplo código #

```
# -*- encoding: utf-8 -*-
'''
Un ejemplo de acceso a MySql con jython usando 
zxJDBC (DB Api)
'''

from com.ziclix.python.sql import zxJDBC
bdatos = 'jdbc:mysql://172.30.6.6/poblacion
driver = 'com.mysql.jdbc.Driver'
conexion = zxJDBC.connect(bdatos, 'dai', 'xxx', driver)
cursor = conexion.cursor()

# cuidado con la inyección de código
SQL = '''select m.nom from municipio m, comunidad c
            where m.ca_id = c.ca_id and
            c.nom = ? '''

cursor.execute(SQL, ['Asturias'])
          
for linea in cursor:
    print linea[0]
```

# Ejemplos para trabajar con MySql #
  * http://dev.mysql.com/doc/index-other.html
    * http://downloads.mysql.com/docs/world.sql.zip
# Doc MySql #
  * http://www.slideshare.net/ajdgeniz/mysql-for-developers