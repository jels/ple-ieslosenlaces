# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Usuario(User):
    def __unicode__(self):
        return self.username

class Categoria(models.Model):
    nombre = models.CharField("Categoría", max_length=200)
    def __unicode__(self):
        return self.nombre
        
        
class Pregunta(models.Model):
    categoria = models.ForeignKey(Categoria, 
                                  verbose_name="Categoría a la que pertenece")
    titulo = models.CharField("Título", max_length=200)
    texto = models.TextField("Texto de la pregunta")
    respuesta_1 = models.CharField(max_length=200)
    respuesta_2 = models.CharField(max_length=200)
    respuesta_3 = models.CharField(max_length=200)
    respuesta_4 = models.CharField(max_length=200)
    respuesta_correcta = models.CharField(max_length=200)
    foto = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.titulo
    

class Respuesta(models.Model):
    tiempo = models.IntegerField("Tiempo en segs.")
    resultado = models.IntegerField("0 -> incorrecto, 1 -> correcto")
    pregunta = models.ForeignKey(Pregunta, verbose_name="Pregunta que se responde")
    usuario = models.ForeignKey(User, verbose_name="Usuario que responde")
    
    def __unicode__(self):
        return str(self.pregunta) + " (Usuario: " + str(self.usuario) + ")"
     
