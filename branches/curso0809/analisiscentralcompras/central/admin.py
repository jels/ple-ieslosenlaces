from django.contrib import admin
from models import *

class LineaDocPedidoInLine(admin.TabularInline):
    model = LineaDocPedido
    
class DocPedidoAdmin(admin.ModelAdmin):
    inlines = [LineaDocPedidoInLine,]

# tabla que voy a administrar
admin.site.register(Almacen)
admin.site.register(DocPedido, DocPedidoAdmin)
admin.site.register(Producto)
admin.site.register(LineaDocPedido)
admin.site.register(PrecioProducto)