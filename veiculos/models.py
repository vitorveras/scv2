from django.db import models
from django.urls import reverse


# Create your models here.
# def user_directory_path(instance, filename):
#     file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # return "{0}.png".format(instance.cpf)
class Marca(models.Model):
    descricao = models.CharField('Marca Veículo', max_length=100)

    def __str__(self):
        return self.descricao

    class Meta:
        ordering = ['descricao']
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'


class Modelo(models.Model):
    descricao = models.CharField('Modelo Veículo', max_length=100)

    def __str__(self):
        return self.descricao

    class Meta:
        ordering = ['descricao']
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'


class Cor(models.Model):
    descricao = models.CharField('Cor Veículo', max_length=100)

    def __str__(self):
        return self.descricao

    class Meta:
        ordering = ['descricao']
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'


class Combustivel(models.Model):
    descricao = models.CharField('Combustivel', max_length=20)

    def __str__(self):
        return self.descricao

    class Meta:
        ordering = ['descricao']
        verbose_name = 'Combustível'
        verbose_name_plural = 'Combustíveis'


class Veiculos(models.Model):
    placa = models.CharField('Placa', unique=True, max_length=20)
    descricao = models.CharField('Descricao', max_length=80)
    chassi = models.CharField('Chassi', max_length=200)
    combustivel = models.ForeignKey(Combustivel,on_delete=models.PROTECT, verbose_name='Combustível')
    anofabricacao = models.IntegerField('Ano Fabricação')
    anomodelo = models.IntegerField('Ano Modelo')
    datacompra = models.DateField('Data Aquisição')
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, verbose_name='Marca do Veículo')
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, verbose_name='Modelo do Veículo')
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, verbose_name='Cor do Veículo')
    kmManutencao = models.IntegerField('KM Manutenção Preventiva')

    def __str__(self):
        return self.placa + ' - ' + self.descricao
    
    class Meta:
        ordering            = ['placa']
        verbose_name        = 'Veiculo'
        verbose_name_plural = 'Veiculos'

    def get_absolute_url(self):
        return reverse('veiculos:veiculos-list')
    
