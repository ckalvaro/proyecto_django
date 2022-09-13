from django.urls import path
from AppBlog.views import inicio, noticia_detalle_view, form_noticias, editar_noticia
app_name = 'AppBlog'
urlpatterns = [
    path('', inicio.as_view(), name='inicio'), 
    path('noticia/<int:pk>', noticia_detalle_view.as_view(), name='detalle'),
    path('noticia/nueva_noticia', form_noticias, name='form_noticia'),
    path('noticia/editar/<int:pk>', editar_noticia.as_view(), name='editar_noticia'),
]
