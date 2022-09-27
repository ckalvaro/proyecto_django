from django import forms
from AppBlog.models import Noticia, Comentario
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

class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        labels = {
            'texto':''
        }
        widgets = {
            'texto': forms.Textarea()
        }


class RegistroDeUsuario(UserCreationForm):
    username = forms.CharField(label = "Nombre de usuario *")
    email = forms.EmailField(label = "Correo electrónico *")
    password1 = forms.CharField(label = "Contraseña *", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Repita la contraseña *", widget = forms.PasswordInput)
    web=forms.CharField(required = False, label="Página web")
    descripcion = forms.CharField(required = False, label = "Acerca de mí")

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
    password1 = forms.CharField(label = "Contraseña actual", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Repita la contraseña", widget = forms.PasswordInput)
    web=forms.CharField(label="Modificar página web")
    descripcion = forms.CharField(label = "Modificar Descripción")
    

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]
        help_texts = {k : " " for k in fields}

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="imagen")