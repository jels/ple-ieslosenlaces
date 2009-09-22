from django.db import models

# Create your models here.
class Pedido(models.Model):
    cliente = models.CharField(max_length=120)
    fecha = models.DateField()
    articulos = models.ManyToManyField('Articulo', through='LineaPedido')
    def __unicode__(self):
        return unicode(self.id) + 'de ' + self.cliente

class Articulo(models.Model):
    nombre = models.CharField(max_length=120)
    def __unicode__(self):
        return self.nombre
    

class LineaPedido(models.Model):
    pedido = models.ForeignKey(Pedido)
    articulo = models.ForeignKey(Articulo)
    cantidad = models.IntegerField()
    def num_linea(self):
        arts = self.pedido.articulos.all()
        artsid = [x.id for x in arts]
        return artsid.index(self.articulo.id) +1 
    def __unicode__(self):
        return "%d:%d" % (self.pedido.id, self.num_linea())

    