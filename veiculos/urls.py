from django.urls import path
from . import views

app_name = 'veiculos'

urlpatterns = [
    path("", views.IndexView.as_view(), name="veiculos-list"),
     path("adicionar/", views.CreateView.as_view(), name="veiculos-add"),
     path("editar/<int:pk>/", views.UpdateView.as_view(), name="veiculos-edit"),
     path("remover/<int:pk>/", views.DeleteView.as_view(), name="veiculos-delete"),
     path("<int:pk>/", views.DetailView.as_view(), name="veiculos-show"),
]
