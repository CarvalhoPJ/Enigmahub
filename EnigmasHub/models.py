from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Enigma(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tips = models.TextField()
    correct_answer = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enigmas',default=None, null=True)

    def __str__(self):
        return self.title

class Tentativa(models.Model):
    enigma = models.ForeignKey(Enigma, on_delete=models.CASCADE, related_name='tentativas')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    numero_tentativas = models.IntegerField(default=1)
    esta_correto = models.BooleanField(default=False)
    resultado =models.TextField(default='')

    def __str__(self):
        return f'{self.usuario.username} - {self.enigma.title}'
