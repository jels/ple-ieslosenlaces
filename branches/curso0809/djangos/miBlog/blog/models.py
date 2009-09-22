from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Mensaje(models.Model):
    autor = models.ForeignKey(User)
    titulo = models.CharField(max_length=120)
    cuerpo = models.TextField()
    fech_pub = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.titulo


