from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from ckeditor.fields import RichTextField

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return self.nombre

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
    #un usuario puede tener varios posts, y cada post puede tener varios likes
    likes = models.ManyToManyField(User, related_name='noticia_likes')

    def __str__(self):
        return self.titulo + " por " + str(self.autor)

    def get_absolute_url(self):
        return reverse('AppBlog:detalle', args=(str(self.id)))

    def cantidad_likes(self):
        return self.likes.count()

class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField(blank = True, max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return "Comentario de %s en Noticia %s" % (self.autor, self.noticia.titulo)
        
    def get_success_url(self):
        return reverse_lazy('AppBlog:detalle', kwargs={'pk': self.kwargs['pk']})



class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)  ## se conecta con el usuario
    imagen = models.ImageField(upload_to = "avatares", default = 'default.png', null = True, blank = True)
