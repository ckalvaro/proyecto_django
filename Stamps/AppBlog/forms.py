from django import forms
from AppBlog.models import Noticia

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

