from django.contrib import admin
from .models import  Viagens

# Register your models here.
@admin.register(Viagens)
class ViagensAdmin(admin.ModelAdmin):
    list_display = ('funcionario_solicitante', 'Destino', 'Data_Viagem', 'Hora_Viagem', 'Objetivo', 'Passageiros', 'Km_Inicio', 'Km_Final', 'Veiculo_viag', 'Efetivada','DatahoraSolic')
