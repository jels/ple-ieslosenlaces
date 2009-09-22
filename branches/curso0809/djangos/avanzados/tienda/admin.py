from avanzados.tienda.models import *
from django.contrib import admin

class LineaArticuloInline(admin.TabularInline):
    model = LineaPedido
    extra = 3
    
class PedidoAdmin(admin.ModelAdmin):
    inlines=(LineaArticuloInline,)
    
    
admin.site.register(Articulo)
admin.site.register(Pedido, PedidoAdmin)