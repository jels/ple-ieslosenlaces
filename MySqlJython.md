# Intro MySql #
  * http://es.wikipedia.org/wiki/MySQL
  * http://www.apachefriends.org/es/xampp.html
  * [Guía rápida de administración](http://www.mysql-hispano.org/page.php?id=45)
  * http://www.phpmyadmin.net/home_page/index.php
  * http://dev.mysql.com/doc/refman/5.0/es/index.html

# Driver #
  * http://download.aquafold.com/download/jdbc-drivers/MySQL/

# Conexión con zxJDBC #
http://www.jython.org/docs/zxjdbc.html

# Ejemplo #
```
from com.ziclix.python.sql import zxJDBC
driver="org.gjt.mm.mysql.Driver"
dburl="jdbc:mysql://servidor/db"
con=zxJDBC.connect(dburl,user,passwd,driver)
...
```