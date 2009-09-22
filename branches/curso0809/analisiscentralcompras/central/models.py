# -*- encoding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import User

class Almacen(User):
    eleccionestado = (
                      ('A','Alta'),
                      ('B','Baja'),
                      )
    
    nombre = models.CharField("Nombre", max_length=200)
    estado = models.CharField('Estado', max_length=1, choices=eleccionestado)
    direccion = models.CharField("Direccion", max_length=300)
    fecha_alta = models.DateField("Fecha de alta", auto_now=False, auto_now_add=False, null=True, blank=True)
    fecha_baja = models.DateField("Fecha de baja", auto_now=False, auto_now_add=False, null=True, blank=True)
    def __unicode__(self):
        return self.nombre
    
class DocPedido(models.Model):
    fecha = models.DateTimeField(auto_now=False, auto_now_add=True)
    almacen = models.ForeignKey('Almacen')
    def __unicode__(self):
        return u"%d :: %s :: %s" % (self.id, self.almacen, self.fecha)
    
class Producto(models.Model):
    nombre = models.CharField("Nombre", max_length=75)
    def __unicode__(self):
        return self.nombre
    
class PrecioProducto(models.Model):
    producto = models.ForeignKey('Producto')
    precio = models.DecimalField('Precio ud', max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField('Hasta x uds', max_length=50)
    def __unicode__(self):
        return u"%s :: hasta %d uds :: %.2f" % (self.producto.nombre, self.cantidad, self.precio)
    
class LineaDocPedido(models.Model):
    docpedido = models.ForeignKey('DocPedido')
    producto = models.ForeignKey('Producto')
    cantidad = models.PositiveIntegerField('Cantidad', max_length=50)
    def __unicode__(self):
        return u"%s" % self.producto.nombre