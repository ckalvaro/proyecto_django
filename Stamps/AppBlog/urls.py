from django.urls import path
from AppBlog.views import prueba, form_noticias, noticias

urlpatterns = [
    path('prueba/', prueba, name='prueba'),
    path('form_noticia/', form_noticias, name='form_noticia'),
    path('noticias/', noticias, name='noticias'),
]
