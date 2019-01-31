from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView

from .forms import (
    RequerimentoForm,
    ItemRequeridoFormset,
    AssinaturaFormset,
)
from .models import Requerimento


class RequerimentoCreateView(CreateView):
    model = Requerimento
    form_class = RequerimentoForm
    
    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        itemRequerido_form = ItemRequeridoFormset()
        assinatura_form = AssinaturaFormset()
        return self.render_to_response(
            self.get_context_data(
                form = form,
                itemRequerido_form = itemRequerido_form,
                assinatura_form = assinatura_form
            )
        )

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        itemRequerido_form = ItemRequeridoFormset(self.request.POST)
        assinatura_form = AssinaturaFormset(self.request.POST)
        if (form.is_valid() and itemRequerido_form.is_valid() and assinatura_form.is_valid()):
            return self.form_valid(form, itemRequerido_form, assinatura_form)
        else:
            return self.form_invalid(form, itemRequerido_form, assinatura_form)
    
    def form_valid(self, form, itemRequerido_form, assinatura_form):
        self.object = form.save()
        itemRequerido_form.instance = self.object
        itemRequerido_form.save()
        assinatura_form.instance = self.object
        assinatura_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, itemRequerido_form, assinatura_form):
        return self.render_to_response(
            self.get_context_data(
                form = form,
                itemRequerido_form = itemRequerido_form,
                assinatura_form = assinatura_form
            )
        )
