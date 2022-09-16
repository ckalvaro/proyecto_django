from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return "Categoría " + self.nombre
    
    def get_absolute_url(self):
        return reverse('AppBlog:inicio')



class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    cuerpo = RichTextField(blank = True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    #creacion se determina una sola vez, al crear la noticia. 
    fecha_creacion = models.DateField(auto_now_add=True, auto_now=False, null = True)
    #ultima_modificacion se actualiza cada vez que se guarda un cambio en la noticia
    ultima_modificacion = models.DateTimeField(auto_now_add=False, auto_now=True, null = True)
    categoria = models.CharField(max_length=30, default = 'placeholder')


    def __str__(self):
        return self.titulo + " por " + str(self.autor)
    
    def get_absolute_url(self):
        return reverse('AppBlog:detalle', args=(str(self.id)))

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    nombre_de_usuario = models.CharField(max_length = 80)
    # contraseña1=models.CharField(max_length = 20)
    # contraseña2=models.CharField(max_length = 20)

    def  __str__(self):
        return str(self.nombre_de_usuario)
