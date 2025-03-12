from django import forms
from .models import Viagens
from django.contrib.admin import widgets
from datetime import datetime
from django.utils.timezone import make_aware
from django.forms import TextInput, MultiWidget, DateTimeField

class MinimalSplitDateTimeMultiWidget(MultiWidget):

    def __init__(self, widgets=None, attrs=None):
        if widgets is None:
            if attrs is None:
                attrs = {}
            date_attrs = attrs.copy()
            time_attrs = attrs.copy()

            date_attrs['type'] = 'date'
            time_attrs['type'] = 'time'

            widgets = [
                TextInput(attrs=date_attrs),
                TextInput(attrs=time_attrs),
            ]
        super().__init__(widgets, attrs)

    # nabbing from https://docs.djangoproject.com/en/3.1/ref/forms/widgets/#django.forms.MultiWidget.decompress
    def decompress(self, value):
        if value:
            return [value.date(), value.strftime('%H:%M')]
        return [None, None]

    def value_from_datadict(self, data, files, name):
        date_str, time_str = super().value_from_datadict(data, files, name)
        # DateField expects a single string that it can parse into a date.

        if date_str == time_str == '':
            return None

        if time_str == '':
            time_str = '00:00'

        my_datetime = datetime.strptime(date_str + ' ' + time_str, "%Y-%m-%d %H:%M")
        # making timezone aware
        return make_aware(my_datetime)



class DateInput(forms.DateInput):
    input_type = 'date'

class TimePickerInput(forms.TimeInput):
    input_type = 'time'


class ViagemForm(forms.ModelForm):
    class Meta:
        model = Viagens
        fields = ['Data_Viagem','Hora_Viagem','Destino','Objetivo','Passageiros']
        widgets = {'Data_Viagem': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Selecione a Data',
                       'type': 'date'
                       }),
                'Hora_Viagem': TimePickerInput(),
        }
        localized_fields = ['Data_Viagem']

    # # Validação personalizada opcional
    # def clean(self):
    #     cleaned_data = super().clean()
    #     data_partida = cleaned_data.get('data_partida')
    #     data_atual = date.today()
    #
    #     if data_partida and data_atual and data_partida <= data_atual:
    #         raise forms.ValidationError("A data deve ser maior que a data de hoje.")
    #     return cleaned_data
class ViagemSearchForm(forms.Form):
    Viagems = forms.CharField(label="Digite a Data da Viagem ou Motivo", required=False)


class Viagem_RealizaViagem(forms.ModelForm):
    class Meta:
        model = Viagens
        fields = ['Data_Hora_ini',
                  'Veiculo_viag',
                  'Motorista_viag',
                  'Km_Inicio',
                  'Data_Hora_fim',
                  'Km_Final',
                  'Ocorrencias',
                  
        ]
        widgets = {'Data_Hora_ini': MinimalSplitDateTimeMultiWidget,
                   'Data_Hora_fim': MinimalSplitDateTimeMultiWidget,
                   }

        # widgets = {
        #     'Data_Hora_ini': forms.DateTimeInput(
        #         format=('%Y-%m-%d' ),
        #         attrs={'class': 'form-control',
        #                'placeholder': 'Selecione a Data',
        #                'type': 'date'
        #                }),
        #         'Data_Hora_fim': forms.DateTimeInput(
        #             format=('%Y-%m-%d'),
        #             attrs={'class': 'form-control',
        #                    'placeholder': 'Selecione a Data',
        #                    'type': 'date'
        #                    }),
        #         }