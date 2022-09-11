from django import forms
from AppBlog.models import Noticia

class FormularioNoticia(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'subtitulo', 'cuerpo', 'autor']

