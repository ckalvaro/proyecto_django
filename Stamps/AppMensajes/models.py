from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db.models import Max

# Create your models here.
class Mensaje(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario')
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emisor')
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receptor')
    texto = RichTextField(max_length=1000, blank= True, null=True)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    def enviar_mensaje(m_emisor, m_receptor, m_texto):
        emisor_mensaje = Mensaje(
            usuario = m_emisor,
            emisor = m_emisor,
            receptor = m_receptor,
            texto = m_texto,
            leido = True)
        emisor_mensaje.save()

        receptor_mensaje = Mensaje(
            usuario = m_receptor,
            emisor = m_emisor,
            receptor = m_receptor,
            texto = m_texto)
        receptor_mensaje.save()

        return emisor_mensaje

    def get_mensajes(user):
        usuarios = []
        mensajes = Mensaje.objects.filter(usuario = user).values('receptor').annotate(ultimo_mensaje = Max('fecha_envio')).order_by('-ultimo_mensaje')
        for mensaje in mensajes:
            usuarios.append({
                'usuario': User.objects.get(pk = mensaje['receptor']),
                'no_leidos': Mensaje.objects.filter(usuario = user, receptor__pk= mensaje['receptor'], leido = False).count(),
                'ult_mensaje': mensaje['ultimo_mensaje']
            })
        return usuarios