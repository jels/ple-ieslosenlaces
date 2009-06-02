from django.conf.urls.defaults import *
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^analisiscentralcompras/', include('analisis.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^/?$', 'analisiscentralcompras.central.views.index'),
    (r'^index$', 'analisiscentralcompras.central.views.index'),
    (r'^contacto$', 'analisiscentralcompras.central.views.contacto'),
    (r'^login$', 'analisiscentralcompras.central.views.login',
     {'template_name': 'login.html'}),
    (r'^catalogo$', 'analisiscentralcompras.central.views.catalogo'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    (r'^logout$', 'analisiscentralcompras.central.views.milogout') ,
)
