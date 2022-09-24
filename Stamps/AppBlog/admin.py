from django.contrib import admin
from AppBlog.models import Noticia, Categoria, Comentario, Avatar
# Register your models here.
admin.site.register(Noticia)
admin.site.register(Categoria)
admin.site.register(Comentario)
admin.site.register(Avatar)
