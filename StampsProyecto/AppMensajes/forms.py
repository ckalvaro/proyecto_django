from django import forms
from .models import Conversacion, Mensaje

class FormularioConversacion(forms.Form):
    model = Conversacion
    username = forms.CharField(max_length=100, label='')

class FormularioMensaje(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['body']
        labels = {
            'body': '',
        }
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }



    