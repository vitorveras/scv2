from django import forms
from .models import Motorista
from datetime import date

class DateInput(forms.DateInput):
    input_type = 'date'

class TimePickerInput(forms.TimeInput):
    input_type = 'time'


class MotoristaForm(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = '__all__'
        widgets = {'Data_Nascimento': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Selecione a Data',
                       'type': 'date'
                       }),
                'Data_Vencimento': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Selecione a Data',
                       'type': 'date'
                       }),
            'CPF': forms.TextInput(attrs={'data-mask': "000.000.000-00"}),
        }
        localized_fields = ['Nome_Motorista']

    # # Validação personalizada opcional
    # def clean(self):
    #     cleaned_data = super().clean()
    #     data_partida = cleaned_data.get('data_partida')
    #     data_atual = date.today()
    #
    #     if data_partida and data_atual and data_partida <= data_atual:
    #         raise forms.ValidationError("A data deve ser maior que a data de hoje.")
    #     return cleaned_data
class MotoristaSearchForm(forms.Form):
    Motoristas = forms.CharField(label="Digite o Nome do Motorista", required=False)