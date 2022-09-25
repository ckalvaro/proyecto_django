# proyecto_django

proyecto final coderhouse

### Para crear base de datos, ingresar a la terminal:

    python manage.py migrate

#Para dar de alta el panel de Administrador, ingresar en la terminal:

    python manage.py createsuperuser

### Para crear y administrar los modelos en la base de datos:

1- En admin.py hacer importación de models:

    from django.contrib import admin
    from .models import *
    
2- En admin.py agregar todos los modelos de la siguiente forma:

    admin.site.register(Nombre_de_objeto)
