from django.urls import path
from AppBlog.views import prueba

urlpatterns = [
    path('prueba/', prueba, name='prueba'),
]
