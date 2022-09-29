from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.
class Conversacion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")

    def __str__(self):
        return "Conversacion entre " + str(self.user) + " y " + str(self.receiver)

class Mensaje(models.Model):
    conversacion = models.ForeignKey(Conversacion, on_delete=models.CASCADE, blank=True, null=True)
    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    body = RichTextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Mensaje de " + str(self.sender_user) + " para " + str(self.receiver_user)