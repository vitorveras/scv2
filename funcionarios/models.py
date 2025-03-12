from django.contrib import admin
from django.db import models
from django.conf import settings
from django.contrib.auth import views

# Create your models here.
class Setor(models.Model):
    nome    = models.CharField('Nome', max_length=100)
    sigla   = models.CharField('Sigla', max_length=50)
    admin   = models.BooleanField('Pode Autorizar Viagens', default=False)

    class Meta:
        verbose_name        = 'Setor'
        verbose_name_plural = 'Setores'
        ordering            = ['sigla']
    
    def __str__(self):
        return self.sigla

class Funcionario(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    setor   = models.ForeignKey(Setor, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Setor', related_name='funcionarios')

    class Meta:
        verbose_name        = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
        ordering            = ['usuario__username']

    def __str__(self):
        return f'{self.usuario.username}'