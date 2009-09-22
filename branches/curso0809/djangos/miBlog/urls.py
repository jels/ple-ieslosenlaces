from django.conf.urls.defaults import *
from blog.views import hola, hora, hora_menos_uno, hora_mas, hora_mas_t, lista_empleados

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^miBlog/', include('miBlog.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^saludo/$', hola),
    (r'^ahora/$', hora),
    (r'^canarias/$', hora_menos_uno),
    (r'^ahora/mas/(\d+)/$', hora_mas_t),
    (r'^empleados/$', lista_empleados),
)
