from django import forms
from AppBlog.models import Noticia, Categoria

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

    