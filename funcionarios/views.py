from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import SetorForm, FuncionarioForm
from django.conf import settings
from .models import Setor, Funcionario
from django.contrib.auth.decorators import login_required
from .decorators import adminstaff_required

# Create your views here.
#Setores
@login_required
@adminstaff_required
def novoSetor(request):
    form = SetorForm(request.POST or None)
    if form.is_valid():
            form.save()
            return redirect('listarSetores')
 
    context = { 'sysid': settings.SYSID,'selecionado': 'setor', 'form': form, 'texto': 'Novo'}
    return render(request, 'setor/form.html', context)


@login_required
@adminstaff_required
def editarSetor(request, id):
    setor = get_object_or_404(Setor, pk=id)
    form = SetorForm(request.POST or None, instance=setor)

    if form.is_valid():
        form.save()
        return redirect('listarSetores')
 
    context = { 'sysid': settings.SYSID,'selecionado': 'setor', 'form': form, 'texto': 'Editar'}
    return render(request, 'setor/form.html', context)

@login_required
@adminstaff_required
def listarSetores(request):
    setores = Setor.objects.all().order_by('sigla')

    context = { 'sysid': settings.SYSID,'selecionado': 'setor', 'setores': setores}
    return render(request, 'setor/lista.html', context)

@login_required
@adminstaff_required
def removerSetor(request, id):
    setor = get_object_or_404(Setor, pk=id)
    if request.method=='POST':
        setor.delete()
        return redirect('listarSetores')
    context = { 'sysid': settings.SYSID,'selecionado': 'setor', 'setor': setor}
    return render(request, 'setor/remover.html', context)

#Funcionários
@login_required
@adminstaff_required
def novoFuncionario(request):
    form = FuncionarioForm(request.POST or None)
    if form.is_valid():
            form.save()
            return redirect('listarFuncionarios')
 
    context = { 'sysid': settings.SYSID,'selecionado': 'funcionario', 'form': form, 'texto': 'Novo'}
    return render(request, 'funcionario/form.html', context)

@login_required
@adminstaff_required
def editarFuncionario(request, id):
    funcionario = get_object_or_404(Funcionario, pk=id)
    form = FuncionarioForm(request.POST or None, instance=funcionario)

    if form.is_valid():
        form.save()
        return redirect('listarFuncionarios')
 
    context = { 'sysid': settings.SYSID,'selecionado': 'funcionario', 'form': form, 'texto': 'Editar'}
    return render(request, 'funcionario/form.html', context)

@login_required
@adminstaff_required
def listarFuncionarios(request):
    funcionarios = Funcionario.objects.all().order_by('setor','usuario__first_name')

    context = { 'sysid': settings.SYSID,'selecionado': 'funcionario', 'funcionarios': funcionarios}
    return render(request, 'funcionario/lista.html', context)

@login_required
@adminstaff_required
def removerFuncionario(request, id):
    funcionario = get_object_or_404(Funcionario, pk=id)
    if request.method=='POST':
        funcionario.delete()
        return redirect('listarFuncionarios')
    context = { 'sysid': settings.SYSID,'selecionado': 'funcionario', 'funcionario': funcionario}
    return render(request, 'funcionario/remover.html', context)
