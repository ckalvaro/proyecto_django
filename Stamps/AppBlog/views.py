from django.shortcuts import render
from AppBlog.models import Noticia
from AppBlog.forms import FormularioNoticia

# Create your views here.
def prueba(request):
    return render(request, 'AppBlog/index.html')

def form_noticias(request):
    if request.method == 'POST':
        form = FormularioNoticia(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            titulo = info.get('titulo')
            subtitulo = info.get('subtitulo')
            cuerpo = info.get('cuerpo')
            autor_nombre = info.get('autor_nombre')
            noticia = Noticia(titulo = titulo, subtitulo = subtitulo, cuerpo = cuerpo, autor_nombre = autor_nombre)
            noticia.save()
            mensaje = "Carga exitosa"
            return render(request, 'AppBlog/formulario_noticia.html', {'mensaje':mensaje})
    else:
        form = FormularioNoticia()
        mensaje = "Rellene el formulario"
        return render(request, 'AppBlog/formulario_noticia.html', {'mensaje':mensaje, 'form':form})

def noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'AppBlog/noticias.html', {'noticias':noticias})