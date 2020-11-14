from django import forms
from .models import *


class TonnersForm(forms.ModelForm):
    class Meta:
        model = Tonners
        fields = ['descricao', 'quantidade']


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['empresa']


class SetorForm(forms.ModelForm):
    class Meta:
        model = Setor
        fields = ['setor']


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['categoria']


class AberturaForm(forms.ModelForm):
    class Meta:
        model = Abertura
        fields = ['status']

