from django.urls import path
from . import views

app_name = 'motoristas'

urlpatterns = [
    path("", views.IndexView.as_view(), name="motorista-list"),
     path("adicionar/", views.CreateView.as_view(), name="motorista-add"),
     path("editar/<int:pk>/", views.UpdateView.as_view(), name="motorista-edit"),
     path("remover/<int:pk>/", views.DeleteView.as_view(), name="motorista-delete"),
     path("<int:pk>/", views.DetailView.as_view(), name="motorista-show"),
]
