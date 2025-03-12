from django import forms
from .models import Veiculos

class DateInput(forms.DateInput):
    input_type = 'date'

class VeiculosForm(forms.ModelForm):
    class Meta:
        model = Veiculos
        fields = ['placa','descricao', 'combustivel', 'chassi', 'anomodelo', 'anofabricacao','datacompra','marca','modelo','cor','kmManutencao']
        widgets = {
            'datacompra': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Selecione a Data',
                       'type': 'date'
                       }),
        }
        localized_fields = ['descricao']

class VeiculosSearchForm(forms.Form):
    veiculo = forms.CharField(label="Digite a Descrição do Veiculo ou a Placa", required=False)