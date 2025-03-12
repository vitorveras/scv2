from django.db import models
from django.urls import reverse
from cpf_field.models import CPFField

# Create your models here.
class Motorista(models.Model):
    Nome_Motorista  = models.CharField('Nome do Motorista', max_length=200)
    CPF             = CPFField('CPF do Motorista', max_length=20)
    Data_Nascimento = models.DateField('Data de Nascimento')
    CNH             = models.CharField('Carteira de Habilitação', blank=False, null=False)
    Data_Vencimento = models.DateField('Data Vencimento CNH', blank=False, null=False)
    Categoria       = models.CharField('Categoria da CNH', blank=False, null=False)
    Telefone        = models.CharField('Telefone do Motorista', blank=False, null=False)

    def Data_Nascimento_Format(self):
        if self.Data_Nascimento is None:
                return ''
        else:
                return f'{self.Data_Nascimento.__format__("%d/%m/%Y")}'

    def Data_Vencimento_Format(self):
        if self.Data_Vencimento is None:
                return ''
        else:
                return f'{self.Data_Vencimento.__format__("%d/%m/%Y")}'

    def __str__(self):
        return f'{self.Nome_Motorista}  -  {self.CPF}'
    class Meta:
        ordering = ['Nome_Motorista']
        verbose_name = 'Motorista'
        verbose_name_plural = 'Motoristas'

    def get_absolute_url(self):
        return reverse('motoristas:motorista-list')