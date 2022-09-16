from django import forms
from AppBlog.models import Noticia, Usuario, Categoria
#crear una lista con todas las categorias
opciones = Categoria.objects.all().values_list('nombre', 'nombre')
#esto retorna un queryset, hay que 'limpiar' los datos para trabajar más cómodos
lista_opciones = []
for opcion in opciones:
    lista_opciones.append(opcion)

class FormularioNoticia(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'subtitulo','categoria', 'cuerpo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(choices = lista_opciones, attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
        }

class FormularioUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'nombre_de_usuario']

        # widgets = {
        #     'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
        #     'apellido' : forms.TextInput(attrs={'class' : 'form-control'}),
        #     'email' : forms.EmailField(attrs={'class' : 'form-control'}),
        #     'nombre_de_usuario' : forms.TextInput(attrs={'class' : 'form-control'}),
        #     'contraseña1' : forms.TextInput(attrs={'class' : 'form-control'}),
        #     'contraseña2' : forms.TextInput(attrs={'class' : 'form-control'}),
        # }
