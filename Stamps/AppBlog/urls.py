from django.urls import path
from AppBlog.views import prueba, form_noticias, noticias, form_usuarios, usuarios

urlpatterns = [
    path('prueba/', prueba, name='prueba'),
    path('form_noticia/', form_noticias, name='form_noticia'),
    path('noticias/', noticias, name='noticias'),
    path('form_usuario/', form_usuarios, name= 'form_usuario'),
    path('usuarios/', usuarios, name = 'usuarios'),
]
