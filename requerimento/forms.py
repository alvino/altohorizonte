from django import forms
from django.forms.models import inlineformset_factory

from .models import (
    Secretaria,
    CentroCusto,
    Requerimento,
    Produto, 
    ItemRequerido,
    assinante, 
    Assinatura,
)


class ItemRequeridoForm(forms.ModelForm):
    class Meta:
        model = ItemRequerido
        fields = ['quantidade', 'unidade', 'produto']
        

class AssinaturaForm(forms.ModelForm):
    class Meta:
        model = Assinatura
        fields = ['assinante']


class RequerimentoForm(forms.ModelForm):
    class Meta:
        model = Requerimento
        fields = ['origem', 'destino', 'justificativa']
        widgets = {
            'justificativa':forms.Textarea(attrs={'rows':5, 'cols':80,}),
        }

ItemRequeridoFormset = forms.formset_factory(ItemRequeridoForm, min_num=1)
AssinaturaFormset = forms.formset_factory(AssinaturaForm, min_num=1)