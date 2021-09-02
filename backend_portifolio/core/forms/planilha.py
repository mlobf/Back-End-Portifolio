from django.forms import ModelForm
from core.models import Planilha
from django import forms


class PlanilhaForm(ModelForm):
    class Meta:
        model = Planilha
        fields = ['external_key', 'client_name', 'file']


class PlanihaDateForm(forms.Form):
    data_inicial = forms.DateField()
