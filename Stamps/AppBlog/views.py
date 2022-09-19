from django.shortcuts import render, redirect, get_object_or_404
from AppBlog.models import Noticia
from AppBlog.forms import FormularioNoticia
from django.views.generic import DetailView, UpdateView, ListView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from AppBlog.models import Noticia
from AppBlog.forms import FormularioNoticia
from AppBlog.models import Categoria
from django.http import HttpResponseRedirect 


# Create your views here.
class inicio(ListView):
    model = Noticia
    template_name = 'AppBlog/inicio_app_blog.html'
    ordering = ['-fecha_creacion'] #ORDENA DE MAYOR A MENOR SEGUN fecha_creacion

class noticia_detalle_view(DetailView):
    model = Noticia
    template_name = 'AppBlog/noticia_detalle.html'

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

def like_noticia(request, pk):
    noticia = get_object_or_404(Noticia, id = request.POST.get('noticia_like'))
    noticia.likes.add(request.user)
    return HttpResponseRedirect(reverse('AppBlog:detalle' , args=(str(pk))))

#def eliminar_usuario(request, id):
    #usuario = Usuario.objects.get(id = id)
    #usuario.delete()
    #usuarios=Usuario.objects.all()
    #return render(request, 'AppBlog/usuarios.html', {'usuarios': usuarios})


#def editar_usuario(request, id):
    #usuario=Usuario.objects.get(id = id)
    #if request.method == "POST":
        #form = FormularioUsuario(request.POST)
        #if form.is_valid():
            #info = form.cleaned_data
            #usuario.nombre = info["nombre"]
            #usuario.apellido = info["apellido"]
            #usuario.email = info["email"]
            #usuario.nombre_de_usuario = info["nombre_de_usuario"]
            #usuario.save()
            #usuarios=Usuario.objects.all()
            #mensaje = "Usuario editado exitosamente"
            #return render(request, 'AppBlog/usuarios.html', {'usuarios': usuarios, 'mensaje': mensaje})
    #else:
        #form = FormularioUsuario( initial = { 
            #"nombre" : usuario.nombre, 
            #"apellido" : usuario.apellido,
            #"email" : usuario.email,
            #"nombre_de_usuario" : usuario.nombre_de_usuario, 
        
        #})

        #return render (request, 'AppBlog/editar_usuario.html', {
            #"formulario": form, 
            #"nombre" : usuario.nombre,
            #"id" : usuario.id, 
            # "apellido" : usuario.apellido,    
            # "email" : usuario.email,
            # "nombre_de_usuario" : usuario.nombre_de_usuario,
        #})

#def login_view(request):
    #if request.method == "POST":
        #form = InicioDeUsuario(request, data = request.POST)
        #if form.is_valid():
            #usuario = request.POST["username"]
            #clave=request.POST["password"]
            #usuario_logueado= authenticate(username = usuario, password = clave)
            #if usuario_logueado is not None:
                #login (request, usuario_logueado)
                #mensaje = "Bienvenido {usuario_logueado}"
                #return render (request, 'AppBlog/inicio_app_blog.html', {"mensaje" : mensaje} )
            #else:
                #mensaje = "Usuario o contraseña incorrectos"
                #return render (request, 'AppBlog/login.html', {"mensaje": mensaje, "form" : form})
        #else:
            #return render(request, 'AppBlog/login.html', {"form": form})
    #else:
        #form=InicioDeUsuario()
        #return render (request, 'AppBlog/login.html', {"form" : form})


#def registro(request):
    #if request.method == "POST":
        #form = RegistroDeUsuario(request.POST)
        #if form.is_valid():
            #username = form.cleaned_data["username"]
            #form.save()
            #mensaje = "Usuario {username} creado"
            #return render (request, 'AppBlog/inicio_app_blog.html/', {"mensaje" :  mensaje})
    #else:
        #form = RegistroDeUsuario()
        #return render (request, 'AppBlog/registro.html', {"form" : form})