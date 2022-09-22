from django.urls import path
from AppBlog.views import inicio, noticia_detalle_view, form_noticias, editar_noticia, eliminar_noticia, NuevaCategoriaView, login_view, registro, editar_usuario, like_noticia, form_comentarios, lista_categoria
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LogoutView

app_name = 'AppBlog'
urlpatterns = [
    path('', inicio.as_view(), name='inicio'), 
    path('noticia/<int:pk>', noticia_detalle_view.as_view(), name='detalle'),
    path('noticia/nueva_noticia', form_noticias, name='form_noticia'),
    path('noticia/nueva_categoria', NuevaCategoriaView.as_view(), name='form_categoria'),
    path('noticia/categoria/<str:cat>', lista_categoria, name='lista_categoria'),
    path('noticia/editar/<int:pk>', editar_noticia.as_view(), name='editar_noticia'),
    path('noticia/eliminar/<int:pk>', eliminar_noticia.as_view(), name='eliminar_noticia'),
    #path('form_usuario/', form_usuarios, name= 'form_usuario'),
    #path('usuarios/', usuarios, name = 'usuarios'),
    path('editar_usuario/', editar_usuario, name = 'editar_usuario'),
    #path('eliminar_usuario/<id>', eliminar_usuario, name = 'eliminar_usuario'),
    path('login/', login_view, name='login'),
    path('registro/', registro, name = 'registro'),
    path('logout/', LogoutView.as_view(template_name ='AppBlog/inicio_app_blog.html'), name='logout'),
    path('noticia/like/<int:pk>', like_noticia, name='like_noticia'),
    path('noticia/<int:pk>/nuevo_comentario', form_comentarios.as_view(), name='form_comentario'),
]

# urlpatterns += staticfiles_urlpatterns()