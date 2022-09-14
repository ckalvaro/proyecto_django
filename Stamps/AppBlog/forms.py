from django import forms
from AppBlog.models import Noticia, Usuario

class FormularioNoticia(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'subtitulo', 'cuerpo', 'autor_nombre']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
            'autor_nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class FormularioUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'nombre_de_usuario', 'contraseña1', 'contraseña2' ]

        widgets = {
            'nombre' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'apellido' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'email' : forms.EmailField(attrs = {'class' : 'form-control'}),
            'nombre_de_usuario' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'contraseña1' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'contraseña2' : forms.TextInput(attrs = {'class' : 'form-control'}),
        }
