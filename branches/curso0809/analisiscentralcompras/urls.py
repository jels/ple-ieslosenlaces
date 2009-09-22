from django.conf.urls.defaults import *
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

admin.site.root_path="/central/admin/"

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
    (r'^logout$', 'analisiscentralcompras.central.views.milogout'),
    (r'^alta$', 'analisiscentralcompras.central.views.alta'),
    (r'^alta_pedido$', 'analisiscentralcompras.central.views.alta_pedido'),
    (r'^pedido$', 'analisiscentralcompras.central.views.pedido'),
    (r'^detallepedido/(\d+)/$', 'analisiscentralcompras.central.views.detallepedido'),
    (r'^historico$', 'analisiscentralcompras.central.views.historico'),
    (r'^thanks/$', 'analisiscentralcompras.central.views.thanks'),
    (r'^enviado_pedido$', 'analisiscentralcompras.central.views.enviado_pedido'),
    (r'^catalogo$', 'analisiscentralcompras.central.views.catalogo'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)
