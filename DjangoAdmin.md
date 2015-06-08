
# ¿Qué es? #
Aplicación [CRUD](http://es.wikipedia.org/wiki/CRUD) automática sobre el diseño de nuestro modelo.
# Instalar admin #
Añadir en `settings.py`
```
INSTALLED_APPS = (
    ...
    'django.contrib.admin',
    ...
```
Añadir la url a `urls.py`
```
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
)
```
Creación de `admin.py` dentro de la aplicación que queremos administrar:
```
from django.contrib import admin
from models import Mensaje

# Clase que voy a administrar
admin.site.register(Mensaje)
```
```
manage.py syncdb
```

# Adaptando el formato de admin #
## ¿Qué va a salir en los listados y formularios? ##
```
from django.contrib import admin
from models import Mensaje
class MensajeAdmin(admin.ModelAdmin):
    fields = ('titulo', 'cuerpo')
    list_display = ('titulo', 'autor', 'fech_pub')
    date_hierarchy = 'fech_pub'
admin.site.register(Mensaje, MensajeAdmin)
```
  * **fields** restringe los campos en los formularios para añadir/editar. También se puede usar **exclude**
  * **list\_display** especifica qué campos (o métodos) se muestran en el listado de mensajes. Si nos especifica, se muestra el `__unicode__` del modelo.
  * **date\_hierarchy** permite ver los detalles de una campo fecha.
Añadirmos el autor de forma automática cuando se crea un nuevo mensaje (no cuando se modifica).
## Autor automático ##
```
def save_model(self, request, obj, form, change):
    if not change:
        obj.autor = request.user
    obj.save()
```
## Modificacmos encabezados de listados ##
En `blog/models.py`:
```
    fech_pub = models.DateTimeField(u'Fecha publicación', auto_now_add=True)
    fech_mod = models.DateTimeField(u'Fecha modificación', auto_now=True) 
```