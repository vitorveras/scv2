from django.contrib import admin

from .models import  Motorista
# Register your models here.
@admin.register(Motorista)
class MotoristaAdmin(admin.ModelAdmin):
    list_display = ('Nome_Motorista', 'CPF')

