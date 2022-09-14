from django.urls import path
<<<<<<< HEAD
from AppBlog.views import inicio, noticia_detalle_view, form_noticias, editar_noticia, eliminar_noticia
app_name = 'AppBlog'
urlpatterns = [
    path('', inicio.as_view(), name='inicio'), 
    path('noticia/<int:pk>', noticia_detalle_view.as_view(), name='detalle'),
    path('noticia/nueva_noticia', form_noticias, name='form_noticia'),
    path('noticia/editar/<int:pk>', editar_noticia.as_view(), name='editar_noticia'),
    path('noticia/eliminar/<int:pk>', eliminar_noticia.as_view(), name='eliminar_noticia'),
=======
from AppBlog.views import prueba, form_noticias, noticias, form_usuarios, usuarios

urlpatterns = [
    path('prueba/', prueba, name='prueba'),
    path('form_noticia/', form_noticias, name='form_noticia'),
    path('noticias/', noticias, name='noticias'),
    path('form_usuario/', form_usuarios, name= 'form_usuario'),
    path('usuarios/', usuarios, name = 'usuarios'),
>>>>>>> 323cd98adf0c9820f1194a5e949c500c9c8df07d
]
