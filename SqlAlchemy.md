# Intro #
## Qué es SqlAlchemy? ##
  * http://www.sqlalchemy.org/
  * http://en.wikipedia.org/wiki/SQLAlchemy : SQLAlchemy is an open source SQL toolkit and object-relational mapper for the Python programming language released under the MIT License.

## Instalar ##
http://www.sqlalchemy.org/docs/intro.html#installing-sqlalchemy
```
easy_install SQLAlchemy
```

```
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
0.6.0
```
## Doc ##
  * http://www.sqlalchemy.org/docs/
  * http://www.sqlalchemy.org/trac/wiki/UsageRecipes
  * http://jythonpodcast.hostjava.net/jythonbook/en/1.0/DatabasesAndJython.html#object-relational-mapping
  * http://www.ibm.com/developerworks/aix/library/au-sqlalchemy/
  * http://www.rmunn.com/sqlalchemy-tutorial/tutorial.html
  * http://cleverdevil.org/elixirtalk/slides.pdf
  * http://files.meetup.com/127119/EssentialSQLAlchemy.pdf
# Primeros pasos #
```
from slqalchemy import *
db = create_engine('mysql+zxjdbc://username:password@localhost/mydb'
```

# Ejemplo completo #
  * http://code.google.com/p/ple-ieslosenlaces/source/browse/trunk/jython/mundo_sqlalchemy.py