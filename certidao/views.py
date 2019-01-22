from django.shortcuts import render
from django.views.generic import ListView

from .models import Link


# view Venda
class LinkList(ListView):
    template_name = 'certidao/link_list.html'
    model = Link