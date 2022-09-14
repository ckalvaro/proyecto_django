from django.urls import path
from AppBlog.views import inicio, noticia_detalle_view, form_noticias, editar_noticia, eliminar_noticia, form_usuarios, usuarios
app_name = 'AppBlog'
urlpatterns = [
    path('', inicio.as_view(), name='inicio'), 
    path('noticia/<int:pk>', noticia_detalle_view.as_view(), name='detalle'),
    path('noticia/nueva_noticia', form_noticias, name='form_noticia'),
    path('noticia/editar/<int:pk>', editar_noticia.as_view(), name='editar_noticia'),
    path('noticia/eliminar/<int:pk>', eliminar_noticia.as_view(), name='eliminar_noticia'),
    path('form_usuario/', form_usuarios, name= 'form_usuario'),
    path('usuarios/', usuarios, name = 'usuarios'),
]