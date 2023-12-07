from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#los modelos ya creados y guardados 
class Curso(models.Model):
    titulo = models.CharField(max_length=40)
    url = models.URLField(null=True)

    def __str__(self):
        return self.titulo


class Historial(models.Model):
    titulo = models.CharField(max_length=40)
    url = models.URLField(null=True)

    def __str__(self):
        return self.titulo


class Artista(models.Model):
    nombre = models.CharField(max_length=40)
    url = models.URLField(null=True)

    def __str__(self):
        return self.nombre
