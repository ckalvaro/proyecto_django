from django.shortcuts import render, redirect
from django.db.models import Q
from django.views import View
from .models import Conversacion, Mensaje
from .forms import FormularioConversacion, FormularioMensaje
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from AppBlog.views import carga_avatar
#importamos carga_avatar para poder ver la foto de perfil en el navbar, aún en una aplicación distinta
# Create your views here.

class ListConversacion(LoginRequiredMixin, View):
    login_url = 'AppBlog:login'
    redirect_field_name = 'AppBlog:login'
    def get(self, request, *args, **kwargs):
        conversaciones = Conversacion.objects.filter(Q(user=request.user) | Q(receiver = request.user))
        context = {
            'conversaciones': conversaciones,
            'imagen': carga_avatar(request)
        }
        return render(request, 'AppMensajes/inbox.html', context)

class CrearConversacion(LoginRequiredMixin, View):
    login_url = 'AppBlog:login'
    redirect_field_name = 'AppBlog:login'
    def get(self, request, *args, **kwargs):
        form = FormularioConversacion()
        context = {
            'formulario': form,
            'imagen': carga_avatar(request)
        }
        return render(request, 'AppMensajes/nueva_conversacion.html', context)

    def post(self, request, *args, **kwargs):
        form = FormularioConversacion(request.POST)
        username = request.POST.get('username')

        try:
            receiver = User.objects.get(username = username)
            if Conversacion.objects.filter(user = request.user, receiver = receiver).exists():
                conversacion = Conversacion.objects.filter(user = request.user, receiver = receiver)[0]
                return redirect('AppMensajes:conversacion', pk = conversacion.pk)
            elif Conversacion.objects.filter(user = receiver, receiver = request.user).exists():
                conversacion = Conversacion.objects.filter(user = receiver, receiver = request.user)[0]
                return redirect('AppMensajes:conversacion', pk = conversacion.pk) 
            if form.is_valid():
                conversacion = Conversacion(
                    user = request.user,
                    receiver = receiver)
                conversacion.save()
                return redirect('AppMensajes:conversacion', pk = conversacion.pk)
        except:
            return redirect('AppMensajes:nueva_conversacion')

class ConversacionView(LoginRequiredMixin, View):
    login_url = 'AppBlog:login'
    redirect_field_name = 'AppBlog:login'
    def get(self, request, pk, *args, **kwargs):
        form = FormularioMensaje()
        conversacion = Conversacion.objects.get(pk = pk)
        lista_mensajes = Mensaje.objects.filter(conversacion__pk__contains = pk)
        context = {
            'conversacion': conversacion,
            'formulario': form,
            'lista_mensajes': lista_mensajes,
            'imagen': carga_avatar(request)
        }

        return render(request, 'AppMensajes/conversacion.html', context)

class CrearMensaje(View):
    def post(self, request, pk, *args, **kwargs):
        conversacion = Conversacion.objects.get(pk=pk)
        if conversacion.receiver == request.user:
            receiver = conversacion.user
        else:
            receiver = conversacion.receiver
        
        mensaje = Mensaje(
            conversacion = conversacion,
            sender_user = request.user,
            receiver_user = receiver,
            body = request.POST.get('body')
        )
        mensaje.save()
        return redirect('AppMensajes:conversacion', pk = pk)

