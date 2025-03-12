from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def Index(request):
    context = {'selecionado': 'inicio'}
    return render(request, 'home.html', context)