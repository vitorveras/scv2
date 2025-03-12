from django.urls import path
from . import views

app_name = 'relatorios'
urlpatterns = [
    path("veiculos/", views.ResumoVeiculos.as_view(), name="resumo-Veiculos"),
    path("motoristas/", views.ResumoMotoristas.as_view(), name="resumo-Motorista"),
    path("solicitantes/", views.ResumoSolicitante.as_view(), name="resumo-Solicitante"),
    path("geral/", views.Geral.as_view(), name="Geral"),
]