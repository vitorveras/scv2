from django.urls import path
from . import views

app_name = 'viagens'

urlpatterns = [
     path("", views.IndexView.as_view(), name="viagens-list"),
     path("adm/list", views.IndexViewPendente.as_view(), name="viagens-list-Pend"),
     # path("listAdm/", views.IndexViewPendenteADM, name="viagens-list-PADM"),
     path("adicionar/", views.CreateView.as_view(), name="viagens-add"),
     path("editar/<int:pk>/", views.UpdateView.as_view(), name="viagens-edit"),
     path("remover/<int:pk>/", views.DeleteView.as_view(), name="viagens-delete"),
     path("exibir/<int:pk>/", views.DetailView.as_view(), name="viagens-show"),
     path("autorizar/<int:pk>/", views.Autoriza, name="viagens-autorizar"),
     path("removerautorizacao/<int:pk>/", views.NaoAutoriza, name="viagens-removerautorizacao"),
     path("adm/autorizar/<int:pk>/", views.AutorizaADM, name="viagens-autorizar-adm"),
     path("adm/naoautorizar/<int:pk>/", views.NaoAutorizaADM, name="viagens-removerautorizacao-adm"),
     path("realizar/<int:pk>/", views.ViagemRealiza, name="viagens-realizar"),
     path("imprimir/<int:pk>/", views.RelatorioViagem, name="viagens-Impressao"),
]