from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Producto(models.Model):
    ID = models.CharField(max_length=120)
    Titulo = models.CharField(max_length=120)
    Precio = models.CharField(max_length=120)

    def __str__(self):
        return self.ID
