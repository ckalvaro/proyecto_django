from django import forms
from .models import Conversacion, Mensaje
from ckeditor.fields import RichTextField

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
        

#class FormularioMensaje(forms.ModelForm):
    #class Meta:
        #model = Mensaje
        #fields = ['body']
        #widgets = {
            #'body': forms.TextInput(attrs={'class': 'form-control'}),
        #}


    