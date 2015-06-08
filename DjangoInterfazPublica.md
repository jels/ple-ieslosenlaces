# Objetivo #
Queremos que nuestra aplicación muestre un listado con los posts más recientes y que podamos ver en detalle uno de ellos con sus comentarios.

# Preparación de urls #
Preparamos urls.py para las nuevas direcciones de nuestra aplicación:
`miBlog/urls.py`
```
 urlpatterns = patterns('',
   (r’^', include(’blog.urls’)),
   (r’^admin/’, include(admin.site.urls)),
) 
```
`blog/urls.py`
```
from django.conf.urls.defaults import *
from models import Mensaje

queryset = {’queryset’: Mensaje.objects.all()}
urlpatterns = patterns(’django.views.generic.list_detail’,
    url('^$', 'object_list', queryset, name="mensajes"),
    url(’^(?P<object_id>\d+)/$’, ‘object_detail’, queryset, name=”mensaje”),
)
```