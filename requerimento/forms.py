from django import forms
from django.forms.models import inlineformset_factory
from django.urls import reverse_lazy

from .models import (
    Secretaria,
    CentroCusto,
    Requerimento,
    ItemRequerido,
    assinante, 
    Assinatura,
)


# class ItemRequeridoForm(forms.ModelForm):
#     class Meta:
#         model = ItemRequerido
#         fields = ['quantidade', 'unidade', 'descricao']
#         widgets = {
#             'descricao':forms.TextInput(attrs={'class':'col-8', }),
#         }    
        

# class AssinaturaForm(forms.ModelForm):
#     class Meta:
#         model = Assinatura
#         fields = ['assinante']
#         widgets = {
#             'assinante':forms.Select(
#                 attrs={'class':'col-4'}
#             ),
#         }


class RequerimentoForm(forms.ModelForm):
    class Meta:
        model = Requerimento
        fields = ['origem', 'destino', 'justificativa']
        widgets = {
            'origem':forms.Select(
                attrs={'class':'form-control'}
            ),
            'destino':forms.Select(
                attrs={'class':'form-control'}
            ),
            'justificativa':forms.Textarea(
                attrs={'class':'form-control', 'rows':5, 'cols':80,}
            ),
        }

ItemRequeridoFormset = inlineformset_factory(
    Requerimento, 
    ItemRequerido, 
    fields=('quantidade', 'unidade', 'descricao', ),
    widgets = {
        'descricao':forms.TextInput(attrs={'class':'col-10', 'list':'descricao_list', }),
    },
    extra=1, 
)
AssinaturaFormset = inlineformset_factory(
    Requerimento, 
    Assinatura, 
    fields=('assinante', ), 
    extra=1, 
)