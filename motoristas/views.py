from django.shortcuts import render
from django.views import generic
from .models import Motorista
from .forms import MotoristaForm, MotoristaSearchForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages


#View que lista todos os visitantes
class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'motoristas/list.html'
    context_object_name = 'motorista'

    def get_queryset(self):
        return Motorista.objects.all().order_by('Nome_Motorista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selecionado"] = 'motoristas'
        return context


class CreateView(LoginRequiredMixin, generic.CreateView):
    model = Motorista
    form_class = MotoristaForm
    template_name = 'motoristas/form.html'
    success_url = reverse_lazy('motoristas:motorista-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selecionado"] = 'motoristas'
        return context

class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Motorista
    form_class = MotoristaForm
    template_name = 'motoristas/form.html'
    success_url = reverse_lazy('motoristas:motorista-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selecionado"] = 'motoristas'
        return context

class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Motorista
    success_url = reverse_lazy('motoristas:motorista-list')
    template_name = 'motoristas/confirm_delete.html'
    context_object_name = 'motorista'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selecionado"] = 'motoristas'
        return context
    

class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Motorista
    template_name = 'motoristas/detail.html'
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selecionado"] = 'motoristas'
        return context
    