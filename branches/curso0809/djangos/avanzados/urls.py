from django.conf.urls.defaults import *
#from accesos.views import logout
from settings import ruta

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^avanzados/', include('avanzados.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^eleccion/$', 'avanzados.coches.views.ajax_color_request'),
    (r'^accesos/login/$', 'django.contrib.auth.views.login', 
      {'template_name': 'accesos/login.html'}),
    (r'^accesos/logout/$', 'avanzados.accesos.views.milogout'),
    (r'^test1/$', 'avanzados.accesos.views.vista1'),
    (r'^accesos/$', 'avanzados.accesos.views.inicio'),
    (r'^bienvenida/$', 'avanzados.coches.views.url_real'),
    (r'^meta/$', 'avanzados.coches.views.meta_info'),
    (r'^/static/(?P<path>.*)$', 'django.views.static.serve', 
     {'document_root': ruta('static')}),
    (r'^catalogo/$', 'avanzados.tienda.views.catalogo'),
    (r'^pedido/$', 'avanzados.tienda.views.pedido'),
)
