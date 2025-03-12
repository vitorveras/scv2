from django import forms
from slick_reporting.forms import BaseReportForm
import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

class GeralReportForm(BaseReportForm, forms.Form):
    start_date = forms.DateField(
        required=True,
        label="Data de início",
        widget= DateInput()    )

    end_date = forms.DateField(
        required=True,
        label="Data do fim",
        widget= DateInput()
    )

    def get_start_date(self):
        return self.cleaned_data.get("start_date")
    def get_end_date(self):
        return self.cleaned_data.get("end_date")
    def get_crispy_helper(self):
        return super().get_crispy_helper()
    
    def get_filters(self):
        filters = {}
        q_filters = []

        return q_filters, filters


class ViagensReportFilterForm(forms.Form):
    start_date = forms.DateField(
        required=True,
        label="Data de início",
        widget= DateInput() )

    end_date = forms.DateField(
        required=True,
        label="Data do fim",
        widget= DateInput() )

    Veiculo_viag = forms.CharField(
        required=False,
        label="Veículo",
        widget=forms.TextInput(attrs={"placeholder": "Descrição do Veículo"}))

    Motorista_viag = forms.CharField(
        required=False,
        label="Motorista",
        widget=forms.TextInput(attrs={"placeholder": "Nome do Motorista"}))

    funcionario_solicitante = forms.CharField(
        required=False,
        label="Funcionário Solicitante",
        widget=forms.TextInput(attrs={"placeholder": "Nome do Funcionário"}))

    def get_start_date(self):
        return self.cleaned_data.get("start_date")

    def get_end_date(self):
        return self.cleaned_data.get("end_date")

    def get_crispy_helper(self):
        return super().get_crispy_helper()

    def get_filters(self):
        filters = {}
        q_filters = []
        return q_filters, filters

