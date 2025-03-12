from django import forms
from .models import Setor, Funcionario

class SetorForm(forms.ModelForm):
    class Meta:
        model = Setor
        fields = ('sigla', 'nome', 'admin')

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ('usuario', 'setor')