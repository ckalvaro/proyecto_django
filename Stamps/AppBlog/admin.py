from django.contrib import admin
from AppBlog.models import Noticia, Categoria, Comentario
# Register your models here.
admin.site.register(Noticia)
admin.site.register(Categoria)
admin.site.register(Comentario)
