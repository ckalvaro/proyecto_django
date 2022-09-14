from django.db import models

# Create your models here.


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    nombre_de_usuario = models.CharField(max_length = 80)
    contraseña1=models.CharField(max_length = 16, min_length = 8)
    contraseña2=models.CharField(max_length = 16, min_length = 8)

    def  __str__(self):
        return str(self.nombre_de_usuario)