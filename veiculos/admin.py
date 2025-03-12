from django.contrib import admin
from .models import  Veiculos, Combustivel, Marca, Modelo, Cor

# Register your models here.
@admin.register(Veiculos)
class VeiculosAdmin(admin.ModelAdmin):
    list_display = ('placa', 'descricao', 'marca', 'modelo', 'cor')


@admin.register(Combustivel)
class CombustivelAdmin(admin.ModelAdmin):
    list_display = ('id','descricao')

@admin.register(Marca)
class CombustivelAdmin(admin.ModelAdmin):
    list_display = ('id','descricao')

@admin.register(Modelo)
class CombustivelAdmin(admin.ModelAdmin):
    list_display = ('id','descricao')

@admin.register(Cor)
class CombustivelAdmin(admin.ModelAdmin):
    list_display = ('id','descricao')
