from django.urls import path, include
from . import views

app_name = 'funcionarios'

urlpatterns = [
    #Setores
    path('setor/novo', views.novoSetor, name='setor-add'),
    path('setor/editar/<int:id>', views.editarSetor, name='setor-edit'),
    path('setor/remover/<int:id>', views.removerSetor, name='setor-delete'),
    path('setor/', views.listarSetores, name='setor-list'),
    #Funcionários
    path('novo', views.novoFuncionario, name='funcionario-add'),
    path('editar/<int:id>', views.editarFuncionario, name='funcionario-edit'),
    path('remover/<int:id>', views.removerFuncionario, name='funcionario-delete'),
    path('', views.listarFuncionarios, name='funcionario-list'),
    

]