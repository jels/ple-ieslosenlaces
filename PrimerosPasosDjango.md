

Basado en el tutorial de Jeff Hui en http://www.bestechvideos.com/2009/04/05/nettuts-diving-into-django y http://blog.jeffhui.net/2009/03/django-blog-tutorial/ .

# Creación del proyecto #
```
django-admin.py startproject <nombre_del_proyecto>
```
Esto crea la siguiente estructura en el nuevo directorio:
```
__init__.py
manage.py
urls.py
settings.py
```
# Configuración de la base de datos #
Para sqlite3 usamos:
```
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'ruta_completa_del_archivo'  
```
Como las rutas tienen que ser absolutas podemos crear/usar la siguente función:
```
import os
def ruta(archivo):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), archivo)
```
# Media #
```
MEDIA_ROOT = ruta('media')
MEDIA_URL = '/recursos/'
TEMPLATE_DIRS = (ruta('templates'),)
```
# Comprobación #
```
python manage.py runserver
```
Lanza la aplicación por defecto en `localhost 8000`
# Crear primera aplicación #
Dentro del directorio del proyecto
```
python manage.py startapp <nombre_proyecto>
```
Activamos el nuevo proyecto en `settings.py`:
```
INSTALLED_APPS = (
     .......
    'blog',
)
```
# Creación de los modelos #
Algo más que **sql**.

Los modelos describen los datos de la aplicación. Son un boceto: explican los tipos de objetos que se van a utilizar, wué campos tienen los objetos y cómo se relacionan. Además tienen metadatos sobre los modelos.
Editamos `proyecto/models.py`:
```
class Mensaje(models.Model):
    autor = models.ForeignKey(User)
    titulo = models.CharField(max_length=120)
    cuerpo = models.TextField()
    fech_pub = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.titulo
```
Para ver el sql que se va a crear:
```
python manage.py validate
python manage.py sql
```
Para crear la estructura en la BD:
```
python manage.py syncdb
```

# Django admin #
DjangoAdmin

# Una aplicación django #
DjangoInterfazPublica

# Tutoriales #
  * http://www.informit.com/articles/article.aspx?p=1273658
  * http://www.cibernatural.com/category/tecnico/tutorial/guia-django/