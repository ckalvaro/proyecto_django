from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, UpdateView, ListView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from AppBlog.forms import FormularioNoticia, RegistroDeUsuario, InicioDeUsuario, UserEditForm, AvatarForm, FormularioComentario
from AppBlog.models import Categoria, Avatar, Noticia
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from AppBlog.models import Comentario

# Create your views here.
class inicio(ListView):
    model = Noticia
    template_name = 'AppBlog/inicio_app_blog.html'
    ordering = ['-fecha_creacion'] #ORDENA DE MAYOR A MENOR SEGUN fecha_creacion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["imagen"] = carga_avatar(self.request)
        return context

class noticia_detalle_view(DetailView):
    model = Noticia
    template_name = 'AppBlog/noticia_detalle.html'
    def get_context_data(self, *args, **kwargs):
        context = super(noticia_detalle_view, self).get_context_data(**kwargs)
        #esto accede a la noticia con ID == a la noticia del detalle
        datos_noticia = get_object_or_404(Noticia, id=self.kwargs['pk'])
        likeado = False
        likes = datos_noticia.cantidad_likes()
        if datos_noticia.likes.filter(id=self.request.user.id).exists():
            likeado = True
        context["cantidad_likes"] = likes
        context["likeado"] = likeado
        context["imagen"] = carga_avatar(self.request)
        return context

#@login_required
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
        return render(request, 'AppBlog/formulario_noticia.html', {'mensaje':mensaje, 'form':form, "imagen": carga_avatar(request)})

def lista_categoria(request, cat):
    noticias_por_categoria = Noticia.objects.filter(categoria=Categoria.objects.get(nombre=cat)).order_by('-fecha_creacion')
    categoria_nombre = cat.title()
    return render(request, 'AppBlog/categoria.html', {'lista_noticias':noticias_por_categoria, 'categoria':categoria_nombre, "imagen":carga_avatar(request)})

class editar_noticia(UpdateView):
    model = Noticia
    template_name = 'AppBlog/editar_noticia.html'
    fields = ['titulo', 'subtitulo','categoria', 'cuerpo']

class eliminar_noticia(DeleteView):
    model = Noticia
    template_name = 'AppBlog/eliminar_noticia.html'
    success_url = reverse_lazy('AppBlog:inicio')


def like_noticia(request, pk):
    noticia = get_object_or_404(Noticia, id = request.POST.get('noticia_like'))
    likeado = False
    if noticia.likes.filter(id=request.user.id).exists():
        noticia.likes.remove(request.user)
        likeado = False
    else:
        noticia.likes.add(request.user)
        likeado = True
    return HttpResponseRedirect(reverse('AppBlog:detalle' , args=(str(pk))))

def login_view(request):
    if request.method == "POST":
        form = InicioDeUsuario(request, data = request.POST)
        if form.is_valid():
            usuario = request.POST["username"]
            clave=request.POST["password"]
            usuario_logueado= authenticate(username = usuario, password = clave)
            if usuario_logueado is not None:
                login (request, usuario_logueado)
                return render (request, 'AppBlog/login.html', {"mensaje" : f"Bienvenido {usuario_logueado}", "imagen":carga_avatar(request)} )
            else:
                return render (request, 'AppBlog/login.html', {"form" : form})
        else:
            return render(request, 'AppBlog/login.html', {"mensaje": "Usuario o contraseña incorrectos","form": form})
    else:
        form=InicioDeUsuario()
        return render (request, 'AppBlog/login.html', {"form" : form })


def registro(request):
    if request.method == "POST":
        form = RegistroDeUsuario(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render (request, 'AppBlog/login.html', {"mensaje" :  f"Usuario {username} creado"})
        else:
            form = RegistroDeUsuario()
            return render (request, 'AppBlog/registro.html', {"form" : form, "mensaje": "Formulario Inválido: La contraseña debe tener, al menos, 8 caracteres, combinar números con letras y minúsculas con mayúsculas"})
    else:
        form = RegistroDeUsuario()
        return render (request, 'AppBlog/registro.html', {"form" : form, "mensaje": "Creá tu usuario para ingresar"})


@login_required
def editar_usuario(request):
    usuario=request.user
    if request.method == "POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.username=info["username"]
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.web=info["web"]
            usuario.descripcion=info["descripcion"]
            usuario.save()
            return render (request, 'AppBlog/inicio_app_blog.html', {"mensaje": f"Perfil de {usuario} editado"})
        else:
            return render(request,'AppBlog/editar_usuario.html', {"mensaje": "Formulario Inválido: La contraseña debe tener, al menos, 8 caracteres, combinar números con letras y minúsculas con mayúsculas", "form": form})
    else:
        form=UserEditForm(instance=usuario)
        return render (request, 'AppBlog/editar_usuario.html', {"form": form, "usuario": usuario, "imagen": carga_avatar(request)})

    ## Se hace función para traer la URL del Avatar ##

def carga_avatar(request):
    imagen = "/media/avatares/default.png"
    if request.user.is_authenticated:
        lista=Avatar.objects.filter(user=request.user)
        if len(lista) != 0:
            imagen = lista[0].imagen.url
    return imagen

    ## view para agregar avatar desde el blog

def agregar_avatar(request):
    if request.method == "POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar_anterior=Avatar.objects.filter(user=request.user)
            if (len(avatar_anterior) > 0):
                avatar_anterior.delete()
            avatar_nuevo = Avatar(user = request.user, imagen = form.cleaned_data["imagen"])
            avatar_nuevo.save()
            return render (request, 'AppBlog/inicio_app_blog.html', {"usuario": request.user, "mensaje": "Avatar cargado"})
    else:
        form = AvatarForm()
    return render (request, 'AppBlog/agregar_avatar.html', {"form": form, "usuario": request.user, "imagen": carga_avatar(request)})

class form_comentarios(CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'AppBlog/formulario_comentario.html'
    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.noticia_id = self.kwargs['pk']
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('AppBlog:detalle', kwargs={'pk': self.kwargs['pk']})


