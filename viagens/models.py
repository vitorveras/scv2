from django.db import models
from django.urls import reverse
from funcionarios.models import Funcionario
from veiculos.models import Veiculos
from motoristas.models import Motorista

class Viagens(models.Model):
    funcionario_solicitante = models.ForeignKey(Funcionario,on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Funcionário Solicitante', related_name='funcionario_solicitante')
    Data_Viagem     = models.DateField('Data da Viagem')
    Hora_Viagem     = models.TimeField('Hora da Viagem')
    Destino         = models.CharField('Destino da Viagem', max_length=500, null=False, blank=False)
    Objetivo        = models.TextField('Objetivo', null=False, blank=False)
    Passageiros     = models.TextField('Passageiros', null=False, blank=False)
    Km_Inicio       = models.IntegerField('KM Inicio', null=True, blank=True)
    Km_Final        = models.IntegerField('KM Fim', null=True, blank=True)
    km_rodado       = models.IntegerField('KM Rodados', blank=True, null=True)
    Veiculo_viag    = models.ForeignKey(Veiculos, on_delete=models.PROTECT, verbose_name='Veiculo Utilizado', null=True, blank=True)
    Motorista_viag  = models.ForeignKey(Motorista, on_delete=models.PROTECT, verbose_name='Motorista', null=True, blank=True)
    Efetivada       = models.BooleanField(default=False,verbose_name='Realizada?', null=True, blank=True)
    Aprovado        = models.BooleanField(default=None,verbose_name='Aprovado', null=True, blank=True)
    Data_Hora_ini   = models.DateTimeField(verbose_name='Data/Hora Saída', null=True, blank=True)
    Data_Hora_fim   = models.DateTimeField(verbose_name='Data/Hora Chegada', null=True, blank=True)
    Ocorrencias     = models.TextField('Ocorrencias', blank=True, null=True)
    DatahoraSolic   = models.DateTimeField(verbose_name='Data/Hora Solicitacao', blank=True, null=True)


    def Data_Viagem_Format(self):
        if self.Data_Viagem is None:
                return ''
        else:
                return f'{self.Data_Viagem.__format__("%d/%m/%Y")}'

    def DatahoraSolic_Format(self):
        if self.DatahoraSolic is None:
                return ''
        else:
                return f'{self.DatahoraSolic.__format__("%d/%m/%Y %H:%M:%S")}'

    def __str__(self):
        return f'{self.Data_Viagem}  -  {self.Objetivo}   - {self.funcionario_solicitante}'

    class Meta:
        ordering = ['Data_Viagem']
        verbose_name = 'Viagem'
        verbose_name_plural = 'Viagens'

    def get_absolute_url(self):
        return reverse('Viagens:Viagens-list')