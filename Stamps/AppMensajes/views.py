from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from AppMensajes.models import Mensaje
from django.http import HttpResponse
from django.template import loader
# Create your views here.
@login_required
def inbox(request):
    usuario = request.user
    mensajes = Mensaje.get_mensajes(usuario) 
    md_activo = None
    mds = None
    if mensajes:
        mensaje = mensajes[0]
        md_activo = mensaje['usuario'].username
        mds = Mensaje.objects.filter(usuario = usuario, receptor = mensaje['usuario'])
        mds.update(leido = True)

        for mensaje in mensajes:
            if mensaje['usuario'].username == md_activo:
                mensaje['no_leidos'] = 0
    
    return render(request,'AppMensajes/mensajes.html',  {'mds' : mds,
            'mensajes' : mensajes,
            'md_activo' : md_activo,})
