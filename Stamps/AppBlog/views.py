from django.shortcuts import render, redirect
from AppBlog.models import Noticia
from AppBlog.forms import FormularioNoticia
from django.views.generic import DetailView, UpdateView, ListView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render
from AppBlog.models import Noticia, Usuario
from AppBlog.forms import FormularioNoticia, FormularioUsuario, RegistroDeUsuario, InicioDeUsuario
from AppBlog.models import Categoria
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
class inicio(ListView):
    model = Noticia
    template_name = 'AppBlog/inicio_app_blog.html'
    ordering = ['-fecha_creacion'] #ORDENA DE MAYOR A MENOR SEGUN fecha_creacion

class noticia_detalle_view(DetailView):
    model = Noticia
    template_name = 'AppBlog/noticia_detalle.html'

@login_required
def form_noticias(request):
    if request.method == 'POST':
        form = FormularioNoticia(request.POST)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.autor = request.user
            noticia.save()
            mensaje = "Carga exitosa"
            return redirect(noticia)
    else:
        form = FormularioNoticia()
        mensaje = "Rellene el formulario"
        return render(request, 'AppBlog/formulario_noticia.html', {'mensaje':mensaje, 'form':form})

class NuevaCategoriaView(CreateView):
    model = Categoria
    template_name = 'AppBlog/nueva_categoria.html'
    fields = '__all__'

class editar_noticia(UpdateView):
    model = Noticia
    template_name = 'AppBlog/editar_noticia.html'
    fields = ['titulo', 'subtitulo','categoria', 'cuerpo']

class eliminar_noticia(DeleteView):
    model = Noticia
    template_name = 'AppBlog/eliminar_noticia.html'
    success_url = reverse_lazy('AppBlog:inicio')
def noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'AppBlog/noticias.html', {'noticias':noticias})

@login_required
def form_usuarios(request):
    if request.method == 'POST':
        form = FormularioUsuario(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info.get('nombre')
            apellido = info.get('apellido')
            email = info.get('email')
            nombre_de_usuario = info.get('nombre_de_usuario')
            # contraseña1 = info.get('contrseña1')
            # contraseña2 = info.get('contrseña2')
            usuario = Usuario (nombre = nombre, apellido = apellido, email = email, nombre_de_usuario = nombre_de_usuario)
            usuario.save()
            mensaje = "Carga exitosa"
            return render(request, 'AppBlog/formulario_usuario.html', {'mensaje':mensaje})
    else:
        form = FormularioUsuario()
        mensaje = "Rellene el formulario"
        return render(request, 'AppBlog/formulario_usuario.html', {'mensaje':mensaje, 'form':form})


def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'AppBlog/usuarios.html', {'usuarios':usuarios})


def eliminar_usuario(request, id):
    usuario = Usuario.objects.get(id = id)
    usuario.delete()
    usuarios=Usuario.objects.all()
    return render(request, 'AppBlog/usuarios.html', {'usuarios': usuarios})


def editar_usuario(request, id):
    usuario=Usuario.objects.get(id = id)
    if request.method == "POST":
        form = FormularioUsuario(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario.nombre = info["nombre"]
            usuario.apellido = info["apellido"]
            usuario.email = info["email"]
            usuario.nombre_de_usuario = info["nombre_de_usuario"]
            usuario.save()
            usuarios=Usuario.objects.all()
            mensaje = "Usuario editado exitosamente"
            return render(request, 'AppBlog/usuarios.html', {'usuarios': usuarios, 'mensaje': mensaje})
    else:
        form = FormularioUsuario( initial = { 
            "nombre" : usuario.nombre, 
            "apellido" : usuario.apellido,
            "email" : usuario.email,
            "nombre_de_usuario" : usuario.nombre_de_usuario, 
        
        })

        return render (request, 'AppBlog/editar_usuario.html', {
            "formulario": form, 
            "nombre" : usuario.nombre,
            "id" : usuario.id, 
            # "apellido" : usuario.apellido,    
            # "email" : usuario.email,
            # "nombre_de_usuario" : usuario.nombre_de_usuario,
        })

def login_view(request):
    if request.method == "POST":
        form = InicioDeUsuario(request, data = request.POST)
        if form.is_valid():
            usuario = request.POST["username"]
            clave=request.POST["password"]
            usuario_logueado= authenticate(username = usuario, password = clave)
            if usuario_logueado is not None:
                login (request, usuario_logueado)
                mensaje = "Bienvenido {usuario_logueado}"
                return render (request, 'AppBlog/inicio_app_blog.html', {"mensaje" : mensaje} )
            else:
                mensaje = "Usuario o contraseña incorrectos"
                return render (request, 'AppBlog/login.html', {"mensaje": mensaje, "form" : form})
        else:
            return render(request, 'AppBlog/login.html', {"form": form})
    else:
        form=InicioDeUsuario()
        return render (request, 'AppBlog/login.html', {"form" : form})


def registro(request):
    if request.method == "POST":
        form = RegistroDeUsuario(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            mensaje = "Usuario {username} creado"
            return render (request, 'AppBlog/inicio_app_blog.html/', {"mensaje" :  mensaje})
    else:
        form = RegistroDeUsuario()
        return render (request, 'AppBlog/registro.html', {"form" : form})