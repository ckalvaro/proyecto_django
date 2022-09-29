from django.urls import path
from .views import ListConversacion, CrearConversacion, ConversacionView, CrearMensaje

app_name = 'AppMensajes'
urlpatterns = [
    path('inbox/', ListConversacion.as_view(), name = 'inbox'),
    path('inbox/crear_conversacion/', CrearConversacion.as_view(), name = 'nueva_conversacion'),
    path('inbox/<int:pk>/', ConversacionView.as_view(), name='conversacion'),
    path('inbox/<int:pk>/crear_mensaje/' , CrearMensaje.as_view(), name = 'crear_mensaje'),
]