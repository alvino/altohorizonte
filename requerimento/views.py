from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView

from .forms import (
    RequerimentoForm,
    ItemRequeridoFormset,
    AssinaturaFormset,
)
from .models import Requerimento, ItemRequerido, Assinatura


class RequerimentoDetailView(DetailView):
    model = Requerimento

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        itens_requeridos = ItemRequerido.objects.filter(requerimento=self.object.pk)
        assinaturas = Assinatura.objects.filter(requerimento=self.object.pk)
        context = self.get_context_data(
            requerimento = self.object,
            itens_requeridos = itens_requeridos,
            assinaturas = assinaturas,
        )
        return self.render_to_response(context)

class RequerimentoListView(ListView):
    model = Requerimento

class RequerimentoCreateView(CreateView):
    success_url = 'requerimento_list'
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
                assinatura_form = assinatura_form,
                descricoes = ItemRequerido.objects.values('descricao').distinct(),
            )
        )

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        itemRequerido_form = ItemRequeridoFormset(self.request.POST, self.request.FILES)
        assinatura_form = AssinaturaFormset(self.request.POST, self.request.FILES)
        if (form.is_valid() and itemRequerido_form.is_valid() and assinatura_form.is_valid()):
            return self.form_valid(form, itemRequerido_form, assinatura_form)
        else:
            return self.form_invalid(form, itemRequerido_form, assinatura_form)
    
    def form_valid(self, form, itemRequerido_form, assinatura_form):
        create_requerimento = form.save()
        itemRequerido_form.instance = create_requerimento
        assinatura_form.instance = create_requerimento
        itemRequerido_form.save()
        assinatura_form.save()
        form.save()
        print(self.success_url)
        return HttpResponseRedirect( 
            reverse_lazy(self.success_url)
        ) 


    def form_invalid(self, form, itemRequerido_form, assinatura_form):
        print('RequerimentoCreateView - form_invalid' )
        return self.render_to_response(
            self.get_context_data(
                form = form,
                itemRequerido_form = itemRequerido_form,
                assinatura_form = assinatura_form
            )
        )
