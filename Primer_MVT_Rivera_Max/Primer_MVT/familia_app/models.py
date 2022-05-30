from django.db import models
from django.forms import CharField

# Create your models here.

class familia(models.Model):

    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dni=models.IntegerField()
    estado=models.CharField(max_length=50)
    fecha=models.CharField(max_length=50)
