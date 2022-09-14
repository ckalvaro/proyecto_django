from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    cuerpo = models.CharField(max_length=2550)
    autor_nombre = models.CharField(max_length=255)
    #creacion se determina una sola vez, al crear la noticia. 
    fecha_creacion = models.DateField(auto_now_add=True, auto_now=False, null = True)
    #ultima_modificacion se actualiza cada vez que se guarda un cambio en la noticia
    ultima_modificacion = models.DateTimeField(auto_now_add=False, auto_now=True, null = True)

    def __str__(self):
        return self.titulo + " - " + str(self.autor_nombre)

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    nombre_de_usuario = models.CharField(max_length = 80)
    contraseña1=models.CharField(max_length = 16, min_length = 8)
    contraseña2=models.CharField(max_length = 16, min_length = 8)

    def  __str__(self):
        return str(self.nombre_de_usuario)