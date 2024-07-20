from django.db import models
from django.contrib.auth.models import User

class Servicios(models.Model):
    nombre = models.CharField(max_length=50)
    tamanio_mascota = models.CharField(max_length=50)
    valor = models.IntegerField()

class Accesorios(models.Model):
    nombre = models.CharField(max_length=50)
    valor = models.IntegerField()

class Clientes(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    nombre_mascota = models.CharField(max_length=60)

class Peluqueros(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=60)

class Avatar(models.Model):   
    imagen = models.ImageField(upload_to="avatares") 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"    

     