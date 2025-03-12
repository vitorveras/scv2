from django.conf import settings
from funcionarios.models import Funcionario
from django.shortcuts import render
from django.contrib import messages


def adminstaff_required(function):
    '''
    Decorator que verifica se o usuário da sessão é membro de algum grupo administrativo.
    '''
    def _function(request, *args, **kwargs):
        funcionario = None
        try:
            funcionario = Funcionario.objects.get(usuario = request.user)
        except:
            pass

        if (funcionario is None or funcionario.setor.admin == False):
            messages.error(request,"Somente usuários com privilégios administrativos")
            context = { 'sysid': settings.SYSID,'selecionado': 'inicio'}
            return render(request, 'home.html', context)
        return function(request, *args, **kwargs)
    return _function