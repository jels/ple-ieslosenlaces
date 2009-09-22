from django.db import models

# Create your models here.

class Color(models.Model):
    color = models.CharField(max_length=256)
    def __unicode__(self):
        return self.color

class Coche(models.Model):
    tipo = models.CharField('Modelo de coche', max_length=256)
    colores = models.ManyToManyField(Color) 
    def __unicode__(self):
        return self.tipo
    