from slick_reporting.views import ReportView, Chart, ListReportView
from slick_reporting.fields import ComputationField
from django.db.models import *
from viagens.models import Viagens
from .forms import GeralReportForm, ViagensReportFilterForm

from django.utils.translation import gettext_lazy as _


def dummy():
    x = _("Filters")
    x = _("Results")
    x = _("From date")
    x = _("To date")
    x = _("Filter")
    x = _("Export to CSV")


class ResumoVeiculos(ReportView):
    report_model = Viagens
    date_field = "Data_Viagem"
    group_by = "Veiculo_viag"
    form_class = GeralReportForm

    columns = [
        "descricao",
        # SlickReportField.create(calculation_method=Sum, "Km_Rodado", "total_Km_Rodado", "Km_Rodado"),
        ComputationField.create(method=Count, field="id", name="quantidade", verbose_name="Quantidade"),
        ComputationField.create(method=Sum, field="km_rodado", name="totalkm", verbose_name="Total Km"),
    ]

    chart_settings = [Chart("Veículo", Chart.PIE, data_source=["quantidade"], title_source=["descricao"])]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selecionado"] = 'relatorios'
        return context
    
    def export_csv(self, report_data):
        return super().export_csv(report_data)
    
    export_csv.title = _("Export to CSV")
    export_csv.icon = "bi bi-filetype-csv"
    export_csv.css_class = "btn-secondary"


class ResumoMotoristas(ReportView):
    report_model = Viagens
    date_field = "Data_Viagem"
    group_by = "Motorista_viag"
    form_class = GeralReportForm

    columns = ["Nome_Motorista",
               ComputationField.create(method=Count, field="id", name="sigla_count", verbose_name="Quantidade"),
               ComputationField.create(method=Sum, field="km_rodado",name="totalkm", verbose_name="Total KM")]

    chart_settings = [Chart("Motorista", Chart.PIE, data_source=["sigla_count"], title_source=["Nome_Motorista"])]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selecionado"] = 'relatorios'
        return context

    def export_csv(self, report_data):
        return super().export_csv(report_data)

    export_csv.title = _("Export to CSV")
    export_csv.icon = "bi bi-filetype-csv"
    export_csv.css_class = "btn-secondary"

class ResumoSolicitante(ReportView):
    report_model = Viagens
    date_field = "Data_Viagem"
    group_by = "funcionario_solicitante"
    form_class = GeralReportForm

    columns = ["usuario__username","setor__sigla",
               ComputationField.create(method=Count, field="id", name="sigla_count", verbose_name="Quantidade"),
               ComputationField.create(method=Sum, field="km_rodado", name="totalkm",verbose_name="Total Km")]

    chart_settings = [Chart("Usuarios Solicitantes", Chart.PIE, data_source=["sigla_count"], title_source=["usuario__username"])]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selecionado"] = 'relatorios'
        return context

    def export_csv(self, report_data):
        return super().export_csv(report_data)

    export_csv.title = _("Export to CSV")
    export_csv.icon = "bi bi-filetype-csv"
    export_csv.css_class = "btn-secondary"


class Geral(ListReportView):
    report_model = Viagens
    columns = [
        "Data_Viagem",
        "Hora_Viagem",
        "funcionario_solicitante__usuario__username",
        "Destino",
        "Objetivo",
        "Passageiros",
        "Veiculo_viag__descricao",
        "Motorista_viag__Nome_Motorista",
        "Km_Inicio",
        "Km_Final",
        "km_rodado",
        "Ocorrencias"
    ]
    date_field = "Data_Viagem"
    template_name = "Viagens_report.html"

    def get_context_data(self, **kwargs):
        # Obter contexto padrão da superclasse
        context = super().get_context_data(**kwargs)
        context["selecionado"] = 'relatorios'

        # Inicializar o formulário com os dados GET
        form = ViagensReportFilterForm(self.request.GET or None)
        context["form"] = form

        return context

    def get_queryset(self):
        # Obter o queryset padrão
        qs = super().get_queryset()
        # Aplicar filtros do formulário
        form = ViagensReportFilterForm(self.request.GET or None)
        if form.is_valid():
            if form.cleaned_data.get("start_date"):
                qs = qs.filter(Data_Viagem__gte=form.cleaned_data["start_date"])
            if form.cleaned_data.get("end_date"):
                qs = qs.filter(Data_Viagem__lte=form.cleaned_data["end_date"])
            if form.cleaned_data.get("Veiculo_viag"):
                qs = qs.filter(Veiculo_viag__descricao__icontains=form.cleaned_data["Veiculo_viag"])
            # Filtro por motorista
            if form.cleaned_data.get("Motorista_viag"):
                qs = qs.filter(Motorista_viag__Nome_Motorista__icontains=form.cleaned_data["Motorista_viag"])
            # Filtro por funcionário solicitante
            if form.cleaned_data.get("funcionario_solicitante"):
                qs = qs.filter(funcionario_solicitante__usuario__username__icontains=form.cleaned_data["funcionario_solicitante"])
        return qs
    
    def export_csv(self, report_data):
        return super().export_csv(report_data)

    export_csv.title = _("Export to CSV")
    export_csv.icon = "bi bi-filetype-csv"
    export_csv.css_class = "btn-secondary"