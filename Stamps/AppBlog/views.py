from django.shortcuts import render, redirect
from AppBlog.models import Noticia
from AppBlog.forms import FormularioNoticia
from django.views.generic import DetailView, UpdateView, ListView, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render
from AppBlog.models import Noticia, Usuario
from AppBlog.forms import FormularioNoticia, FormularioUsuario

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


class editar_noticia(UpdateView):
    model = Noticia
    template_name = 'AppBlog/editar_noticia.html'
    fields = ['titulo', 'subtitulo', 'cuerpo']

class eliminar_noticia(DeleteView):
    model = Noticia
    template_name = 'AppBlog/eliminar_noticia.html'
    success_url = reverse_lazy('AppBlog:inicio')
def noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'AppBlog/noticias.html', {'noticias':noticias})

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
