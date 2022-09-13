from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    #creacion se determina una sola vez, al crear la noticia. 
    fecha_creacion = models.DateField(auto_now_add=True, auto_now=False, null = True)
    #ultima_modificacion se actualiza cada vez que se guarda un cambio en la noticia
    ultima_modificacion = models.DateTimeField(auto_now_add=False, auto_now=True, null = True)

    def __str__(self):
        return self.titulo + " por " + str(self.autor)
    
    def get_absolute_url(self):
        return reverse('AppBlog:detalle', args=(str(self.id)))

