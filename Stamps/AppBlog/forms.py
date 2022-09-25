from django import forms
from AppBlog.models import Noticia
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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


class RegistroDeUsuario(UserCreationForm):
    username = forms.CharField(label = "Nombre de usuario")
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Repita la contraseña", widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k : " " for k in fields}

class InicioDeUsuario(AuthenticationForm):
    username = forms.CharField(label = "Nombre de usuario")
    password = forms.CharField(label = "Contraseña", widget = forms.PasswordInput)
        
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label= "Modificar email")
    username = forms.CharField(label="Cambiar nombre de usuario")
    password1 = forms.CharField(label = "Modificar Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Repita la contraseña", widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]
        help_texts = {k : " " for k in fields}

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="imagen")