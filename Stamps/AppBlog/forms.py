from django import forms
from AppBlog.models import Noticia, Usuario, Categoria
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioNoticia(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'subtitulo','categoria', 'cuerpo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
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

class RegistroDeUsuario(UserCreationForm):
    username = forms.CharField(label = "Nombre de usuario")
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Repita la contraseña", widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k : " " for k in fields}