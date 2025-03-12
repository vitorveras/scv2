from django.shortcuts import render
from django.views import generic
from .models import Veiculos
from .forms import VeiculosForm, VeiculosSearchForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages


#View que lista todos os visitantes
class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'veiculos/list.html'
    context_object_name = 'veiculos'
    def get_queryset(self):
        return Veiculos.objects.all().order_by('placa')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selecionado"] = 'veiculos'
        return context

class CreateView(LoginRequiredMixin, generic.CreateView):
    model = Veiculos
    form_class = VeiculosForm
    template_name = 'veiculos/form.html'
    success_url = reverse_lazy('Veiculos:veiculos-list')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selecionado"] = 'veiculos'
        return context

class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Veiculos
    form_class = VeiculosForm
    template_name = 'veiculos/form.html'
    success_url = reverse_lazy('Veiculos:veiculos-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selecionado"] = 'veiculos'
        return context

class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Veiculos
    success_url = reverse_lazy('Veiculos:veiculos-list')
    template_name = 'veiculos/confirm_delete.html'
    context_object_name = 'veiculos'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selecionado"] = 'veiculos'
        return context
    

class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Veiculos
    template_name = 'veiculos/detail.html'
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selecionado"] = 'veiculos'
        return context
    