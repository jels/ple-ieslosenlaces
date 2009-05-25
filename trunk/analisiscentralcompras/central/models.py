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
    fecha_alta = models.DateField("Fecha de alta", auto_now=False, auto_now_add=False, null=True)
    fecha_baja = models.DateField("Fecha de baja", auto_now=False, auto_now_add=False, null=True)
    def __unicode__(self):
        return self.nombre
    
class DocPedido(models.Model):
    fecha = models.DateTimeField(auto_now=False, auto_now_add=True)
    almacen = models.ForeignKey('Almacen')
    def __unicode__(self):
        pass
    
class Producto(models.Model):
    nombre = models.CharField("Nombre", max_length=75)
    def __unicode__(self):
        return self.nombre
    
class PrecioProducto(models.Model):
    producto = models.ForeignKey('Producto')
    precio = models.PositiveIntegerField('Precio', max_length=50)
    cantidad = models.PositiveIntegerField('Hasta x uds', max_length=50)
    def __unicode__(self):
        return self.producto
    
class LineaDocPedido(models.Model):
    docpedido = models.ForeignKey('DocPedido')
    producto = models.ForeignKey('Producto')
    cantidad = models.PositiveIntegerField('Cantidad', max_length=50)
    def __unicode__(self):
        return self.producto