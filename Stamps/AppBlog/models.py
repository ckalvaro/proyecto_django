from django.db import models
from datetime import datetime, date

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    cuerpo = models.CharField(max_length=2550)
    autor = models.CharField(max_length=255)
    fecha_creacion = models.DateField(auto_now_add=True, auto_now=False, null = True)
    ultima_modificacion = models.DateTimeField(auto_now_add=False, auto_now=True, null = True)
