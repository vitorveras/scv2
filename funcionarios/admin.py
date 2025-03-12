from django.contrib import admin
from .models import Funcionario, Setor

# Register your models here.
@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'setor')
    search_fields = ('usuario',)

@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
    list_display = ('sigla', 'nome')
    search_fields = ('sigla',)
