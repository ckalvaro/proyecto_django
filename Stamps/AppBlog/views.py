from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, UpdateView, ListView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from AppBlog.models import Noticia
from AppBlog.forms import FormularioNoticia, RegistroDeUsuario, InicioDeUsuario, UserEditForm, FormularioComentario
from AppBlog.models import Categoria
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from AppBlog.models import Comentario

# Create your views here.
class inicio(ListView):
    model = Noticia
    template_name = 'AppBlog/inicio_app_blog.html'
    ordering = ['-fecha_creacion'] #ORDENA DE MAYOR A MENOR SEGUN fecha_creacion

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
        return render(request, 'AppBlog/formulario_noticia.html', {'mensaje':mensaje, 'form':form})

class NuevaCategoriaView(CreateView):
    model = Categoria
    template_name = 'AppBlog/nueva_categoria.html'
    fields = '__all__'

def lista_categoria(request, cat):
    noticias_por_categoria = Noticia.objects.filter(categoria=Categoria.objects.get(nombre=cat)).order_by('-fecha_creacion')
    categoria_nombre = cat
    return render(request, 'AppBlog/categoria.html', {'lista_noticias':noticias_por_categoria, 'categoria':categoria_nombre})

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
                return render (request, 'AppBlog/login.html', {"mensaje" : f"Bienvenido {usuario_logueado}"} )
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
            return render (request, 'AppBlog/inicio_app_blog.html', {"mensaje" :  f"Usuario {username} creado"})
        else:
            form = RegistroDeUsuario()
            return render (request, 'AppBlog/registro.html', {"form" : form, "mensaje": "La contraseña debe tener al menos 8 caracteres y combinar números y letras"})
    else:
        form = RegistroDeUsuario()
        return render (request, 'AppBlog/registro.html', {"form" : form, "mensaje": "XXXXX"})


@login_required
def editar_usuario(request):
    usuario=request.user
    if request.method == "POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.save()
            return render (request, 'AppBlog/inicio_app_blog.html', {"mensaje": f"Perfil de {usuario} editado"})
        else:
            return render(request,'AppBlog/inicio_app_blog.html', {"mensaje": "Formulario Inválido", "form": form})
    else:
        form=UserEditForm(instance=usuario)
        return render (request, 'AppBlog/editar_usuario.html', {"form": form, "usuario": usuario})

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


