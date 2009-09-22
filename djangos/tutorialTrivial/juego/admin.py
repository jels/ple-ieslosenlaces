from django.contrib import admin
from models import *

# tabla que voy a administrar
admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Pregunta)
admin.site.register(Respuesta)


