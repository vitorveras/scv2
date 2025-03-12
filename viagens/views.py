import datetime

from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic
from . import views
from .models import Viagens
from .forms import ViagemForm, ViagemSearchForm, Viagem_RealizaViagem
from django.urls import reverse_lazy
from funcionarios.decorators import adminstaff_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from funcionarios.models import Funcionario
from django.contrib import messages

@adminstaff_required
def Autoriza(request, pk):
    viag = get_object_or_404(Viagens, pk=pk)
    viag.Aprovado = True
    viag.save()
    return redirect('viagens:viagens-list')

@adminstaff_required
def NaoAutoriza(request, pk):
    viag = get_object_or_404(Viagens, pk=pk)
    viag.Aprovado = False
    viag.save()
    return redirect('viagens:viagens-list')

@adminstaff_required
def AutorizaADM(request, pk):
    viag = get_object_or_404(Viagens, pk=pk)
    viag.Aprovado = True
    viag.save()
    return redirect('viagens:viagens-list-Pend')

@adminstaff_required
def NaoAutorizaADM(request, pk):
    viag = get_object_or_404(Viagens, pk=pk)
    viag.Aprovado = False
    viag.save()
    return redirect('viagens:viagens-list-Pend')


# Create your views here.

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'viagens/list.html'
    context_object_name = 'Viagens'

    def get_queryset(self):
        return Viagens.objects.all().order_by('Data_Viagem')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selecionado"] = 'viagens'
        return context


class IndexViewPendente(LoginRequiredMixin, generic.ListView):
    template_name = 'viagens/list_adm.html'
    context_object_name = 'Viagens'

    def get_queryset(self):
        # return Viagens.objects.all().order_by('Data_Viagem').filter(Efetivada=False)
        return Viagens.objects.all().order_by('Data_Viagem').filter(Efetivada=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selecionado"] = 'viagens'
        return context


@adminstaff_required
def IndexViewPendenteADM(request):
     print('Entrou')
     queryset = Viagens.objects.all().order_by('Data_Viagem').filter(Efetivada=False)
     context = {'Viagens': queryset, 'selecionado': 'viagens'}
     return render(request, "viagens/list.html", context)


class CreateView(LoginRequiredMixin, generic.CreateView):
    model = Viagens
    form_class = ViagemForm
    template_name = 'viagens/form.html'
    success_url = reverse_lazy('viagens:viagens-list')

    def form_valid(self, form):
        # Atribuir o usuário autenticado ao campo `usuario`
        form.instance.funcionario_solicitante = Funcionario.objects.get(usuario_id=self.request.user.id)
        form.instance.DatahoraSolic = datetime.datetime.now()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selecionado"] = 'viagens'
        return context


class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Viagens
    form_class = ViagemForm
    template_name = 'viagens/form.html'
    success_url = reverse_lazy('viagens:viagens-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selecionado"] = 'viagens'
        return context

class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Viagens
    success_url = reverse_lazy("viagens:viagens-list")
    template_name = 'viagens/confirm_delete.html'
    context_object_name = 'viagem'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selecionado"] = 'viagem'
        return context


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Viagens
    template_name = 'viagens/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selecionado"] = 'viagem'
        return context


@login_required
def ViagemRealiza(request, pk):
    viag = get_object_or_404(Viagens, pk=pk)
    form = Viagem_RealizaViagem(request.POST or None, instance=viag)

    if request.method == 'POST':
        if form.is_valid():
            if viag.Km_Final != None and viag.Km_Final > 0 and viag.Km_Final > viag.Km_Inicio:
                # Calcular Km_Rodado
                viag.km_rodado = viag.Km_Final - viag.Km_Inicio
                viag.Efetivada = True
            form.save()
        return redirect('viagens:viagens-list-Pend')

    return render(
        request=request,
        template_name="viagens/realizar_viagem.html",
        context={"form": form, 'selecionado': viag}
    )

@login_required
def RelatorioViagem(request, pk):
    vig = get_object_or_404(Viagens, pk=pk)
    context = {'selecionado': 'viagem', 'viagem':vig}
    return render(request, 'viagens/impressao.html',context)