from django.urls import path
from usuarios.views import RegistroUser
app_name = 'usuarios'

urlpatterns = [
    path('registro', RegistroUser.as_view(), name='registro'),
]