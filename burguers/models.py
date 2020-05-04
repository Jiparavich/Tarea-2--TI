from django.db import models

# Create your models here.


class Ingrediente(models.Model):

    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=400)

class Hamburguesa(models.Model):

    nombre = models.CharField(max_length=255)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=400)
    imagen = models.URLField(max_length=255)
    ingredientes = models.ManyToManyField(Ingrediente,related_name='hamburguesas', blank=True)