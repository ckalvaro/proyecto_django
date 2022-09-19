from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('AppBlog:inicio')

class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    cuerpo = RichTextField(blank = True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    #creacion se determina una sola vez, al crear la noticia. 
    fecha_creacion = models.DateField(auto_now_add=True, auto_now=False, null = True, blank=True)
    #ultima_modificacion se actualiza cada vez que se guarda un cambio en la noticia
    ultima_modificacion = models.DateTimeField(auto_now_add=False, auto_now=True, null = True, blank=True)
    categoria= models.ForeignKey(Categoria, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo + " por " + str(self.autor)
    
    def get_absolute_url(self):
        return reverse('AppBlog:detalle', args=(str(self.id)))

